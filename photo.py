import os
# import piexif
import pyexiv2
import re
from datetime import datetime
import shutil

reTime1 = {"re": r"(20\d{2}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2})", "format": "%Y-%m-%d-%H-%M-%S"}
reTime2 = {"re": r"(20\d{2}-\d{2}-\d{2} \d{6})", "format": "%Y-%m-%d %H%M%S"}
reTime3 = {"re": r"(20\d{2}-\d{2}-\d{2})", "format": "%Y-%m-%d %H%M%S"}
reTime4 = {"re": r"(20\d{6} \d{6})", "format": "%Y%m%d %H%M%S"}
reTime5 = {"re": r"(20\d{6}_\d{6})", "format": "%Y%m%d_%H%M%S"}
reTime6 = {"re": r"(20\d{12})", "format": "%Y%m%d %H%M%S"}
reTime7 = {"re": r"(20\d{6})", "format": "%Y%m%d"}

rs = (reTime1, reTime2, reTime3, reTime4, reTime5, reTime6, reTime7)
year = "未知时间"


def getTime(path, file_name):
    date_time = None
    for r in rs:
        findall = re.findall(r["re"], file_name)
        if len(findall) > 0:
            date_time = datetime.strftime(datetime.strptime(findall[0], r["format"]), '%Y:%m:%d %H:%M:%S')
            break
    if date_time is None:
        date_time = datetime.strftime(datetime.strptime(year + "0101 000000", '%Y%m%d %H%M%S'), '%Y:%m:%d %H:%M:%S')
    return date_time


def getExif(path):
    for root, dir, files in os.walk(path):
        for file in files:
            try:
                fileStr = str(file)
                full_path = os.path.join(root, file)
                if not fileStr.startswith('.') and not fileStr.lower().endswith(
                        ".mp4") and not fileStr.lower().endswith(
                        ".mov") and not fileStr.lower().endswith(
                    ".rar") and not fileStr.lower().endswith(
                    ".zip"):
                    img = pyexiv2.Image(full_path)
                    exif_dict = img.read_exif()
                    # if "Exif.Photo.DateTimeOriginal" in exif_dict:
                    #     print(exif_dict["Exif.Photo.DateTimeOriginal"])
                    #     print(exif_dict["Exif.Photo.DateTimeDigitized"])
                    # b'2020:12:06 14:08:55' 36868
                    # print(exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal])
                    # print(full_path)
                    # print(not "Exif" in exif_dict)
                    # print(not piexif.ExifIFD.DateTimeOriginal in exif_dict['Exif'])
                    message = ""
                    if not "Exif.Photo.DateTimeOriginal" in exif_dict or not "Exif.Photo.DateTimeDigitized" in exif_dict:
                        time = ""
                        if "Exif.Photo.DateTimeDigitized" in exif_dict:
                            time = exif_dict["Exif.Photo.DateTimeDigitized"]
                        if "Exif.Photo.DateTimeOriginal" in exif_dict:
                            time = exif_dict["Exif.Photo.DateTimeOriginal"]

                        time = getTime(path, fileStr)
                        exif_dict["Exif.Photo.DateTimeDigitized"] = time
                        exif_dict["Exif.Photo.DateTimeOriginal"] = time
                        # img.modify_exif(exif_dict)
                        message += "add " + full_path + " " + time
                    else:
                        message += full_path + " " + exif_dict["Exif.Photo.DateTimeDigitized"]

                    print(message)
                    # img.close()
            except Exception as err:
                print("Error:" + full_path + f"{err}")
                newFile = os.path.join(root, "1", file)
                shutil.move(full_path, newFile)
                print("move %s,%s",full_path,newFile)
                # os.rename(full_path, newFile)

                # if not "EXIF DateTimeOriginal" in exif_dict:
                #     print(123)
                #     # exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = "2020 "
                # else:
                #     originalDate = exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal]
                #     print(originalDate)

                # EXIF DateTimeDigitized
                # if "EXIF DateTimeOriginal" in tags:
                #     print(tags['EXIF DateTimeOriginal'])


# for y in ("2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"):
# for y in ( "2014", "2015", "2016", "2017", "2018", "2019", "2020"):
#     year = y
#     getExif("/Volumes/photo/" + year)
getExif("/Volumes/photo/" + year)

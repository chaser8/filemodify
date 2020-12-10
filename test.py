import re
import os

# s = "2020-11-25 174526.jpg"
# s = "IMG_20201031_142844.jpg"
# s = "1402207955102.jpeg"
# s = "VID_20191231_103312.mp4"
# s = "Camera360_20140323_23"
# s = "C360_2012-04-03-17-19-01.jpg"
# s = "201203173259.jpg"

# s = "Today is 2013-12-12"
# reTime1 = {"re": r"(20\d{2}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2})", "format": "%Y-%m-%d-%H-%M-%S"}
# reTime2 = {"re": r"(20\d{2}-\d{2}-\d{2} \d{6})", "format": "%Y-%m-%d %H%M%S"}
# reTime3 = {"re": r"(20\d{2}-\d{2}-\d{2})", "format": "%Y-%m-%d %H%M%S"}
# reTime4 = {"re": r"(20\d{6} \d{6})", "format": "%Y%m%d %H%M%S"}
# reTime5 = {"re": r"(20\d{6}_\d{6})", "format": "%Y%m%d_%H%M%S"}
# reTime6 = {"re": r"(20\d{12})", "format": "%Y%m%d %H%M%S"}
# reTime7 = {"re": r"(20\d{6})", "format": "%Y%m%d"}
#
# rs = (reTime1, reTime2, reTime3, reTime4, reTime5, reTime6, reTime7)
#
# for r in rs:
#     findall = re.findall(r["re"], s)
#     if len(findall) > 0:
#         print(r["re"])
#         print(findall[0])
#         break

# m = re.match(".*\d{4}-\d{2}-\\d{2}.*",s)
# findall = re.findall(r"(\d{4}-\d{2}-\d{2})", s)
# findall = re.findall(r"(\d{4}-\d{2}-\d{2})", s)
# findall = re.findall(r"(\d{4}-\d{2}-\d{2})", s)
# print(findall)

print(os.path.join("1", "2","3"))

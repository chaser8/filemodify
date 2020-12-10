# -*- coding: utf-8 -*-
import os
import sys
import time
from datetime import datetime
import re

year = "2020"
path = u"/Volumes/photo/" + year
# path = u"/Users/yzb/Downloads/test/"

for root, dir, files in os.walk(path):
    for file in files:
        full_path = os.path.join(root, file)
        if os.path.isfile(full_path):
            ctime = ''
            if (file[0:3] == "IMG" or file[0:3] == "VID") and len(file) > 22:
                # mtime = os.stat(full_path).st_mtime
                # IMG_20120613_194327
                # name = re.findall(r"IMG_(.+?).jpg", file)[0]
                name = file[4:19]
                print(name)
                ctime = datetime.strftime(datetime.strptime(name, '%Y%m%d_%H%M%S'), '%m/%d/%Y %H:%M:%S')
                # print("{0} 修改时间是: {1}".format(full_path,file_modify_time))
            elif file[0:2] == "20" and len(file) > 20:
                name = file[0:17]
                print(name)
                ctime = datetime.strftime(datetime.strptime(name, '%Y-%m-%d %H%M%S'), '%m/%d/%Y %H:%M:%S')
            elif file[0:10] == "Camera360_" and len(file) > 21:
                name = file[10:18] + ' 000000'
                print(name)
                ctime = datetime.strftime(datetime.strptime(name, '%Y%m%d %H%M%S'), '%m/%d/%Y %H:%M:%S')
            elif file[0:5] == "C360_" and len(file) > 21:
                name = file[5:24]
                print(name)
                ctime = datetime.strftime(datetime.strptime(name, '%Y-%m-%d-%H-%M-%S'), '%m/%d/%Y %H:%M:%S')

            if ctime == '':
                ctime = datetime.strftime(datetime.strptime(year + '-01-01-00-00-00', '%Y-%m-%d-%H-%M-%S'),
                                          '%m/%d/%Y %H:%M:%S')

            ml = "SetFile -d '{0}' '{1}'".format(ctime, full_path)
            ml1 = "SetFile -m '{0}' '{1}'".format(ctime, full_path)
            print(ml)
            # file_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))

            os.system(ml)
            os.system(ml1)

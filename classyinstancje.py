#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import glob
import os
import shutil
from builtins import print

class Images(object):
    def __init__(self,source):
        print("init Lista")
        self.path = source

    def loading_list(self):
        image_list = []
        for filename in glob.glob(self.path):
            image = Image.open(filename)
            image_list.append(image)
            path = filename
        return image_list

    def double_folder(self):
        folder_path = r"C:\Python34\Img_checker"
        folder_double = os.path.join(folder_path, "Double")
        if not os.path.exists(folder_double):
            os.mkdir("C:\Python34\Img_checker\Double")
            return 0
        else:
            return -1

    def hgraf(self, image_list):
        for img in list:
            for img_v2 in list:
                if img.histogram == img_v2.histogram and img.filename != img_v2.filename:
                    print("match found", list.index(img), list.index(img_v2))
                    print("match found", os.path.basename(img.filename), os.path.basename(img_v2.filename))
                    list.remove(img_v2)
                    try:
                        shutil.move(os.path.basename(img_v2.filename), "C:\\Python34\\Img_checker\\Double")
                    except WindowsError:
                        pass

rss_path = "C:\\Python34\\Img_checker\\*.jpg"
album = Images(rss_path)

list = album.loading_list()

album.double_folder()
#print("create double: ", album)

album.hgraf(list)

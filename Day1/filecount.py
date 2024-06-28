# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 15:34:36 2018

@author: Balasubramaniam
"""
import os

FilePath=r"F:\yatrabakup\day6"
count=0
for dirpath,dirnames,filenames in os.walk(FilePath):
        print(filenames)
        print(dirnames)
        print(dirpath)
        for dir in dirnames:
            #print(dir)
            for dirpath,dirnames,fnames in os.walk(FilePath+"/"+dir):
                #print(fnames)
                for filename in fnames:
                    #print(filename)
                    (name,extn) = os.path.splitext(filename)
                    #print(extn)

                    if(extn=='.txt'):
                        count=count+1
                        
print(count)
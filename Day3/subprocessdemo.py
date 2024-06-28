# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 06:15:15 2018

@author: Balasubramaniam
"""
import subprocess
result = []
process = subprocess.Popen('dir', 
    shell=True, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE )
for line in process.stdout:
    result.append(line)
errcode = process.returncode
for line in result:
    print(line)



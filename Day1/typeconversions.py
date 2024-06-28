# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 11:21:32 2018

@author: Balasubramaniam
"""
#hexadecimal
memoryAddress=245;
memoryAddress = hex(memoryAddress);
#print("Memory Address=%X\n" %(memoryAddress));

#binary conversion
print(bin(84365));
#int conversion
decimalData=int('10100100110001101',2);
print(decimalData);
#complex number
print(complex(5,67));
decimalData=int(memoryAddress,16);
print(decimalData);

from datetime import date

print(date.today().strftime("%d/%m/%y"))





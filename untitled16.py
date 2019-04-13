# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 20:36:43 2019

@author: admin
"""

n = int(input("enter range"))
sum = 0
for i in range(n):
    x = int(input("enter number"))
    if x % 2!= 0:
        sum = sum + x
print(sum)
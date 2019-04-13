# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 12:12:04 2019

@author: admin
"""
    
a = int(input("enter starting range"))
e = int(input("enter ending range"))
for num in range(a,e+1):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num)
    
# -*- coding: utf-8 -*-
"""
Write a python program to find the biggest and smallest of N
given numbers.
"""
l = []
n = int(input("enter the length"))
Largest = 0
for i in range(n):    
    x = int(input("enter numbers"))
    l.append(x)
    if x > Largest:
        Largest = x
print("largest is",Largest)
smallest = l[0]
for k in l:
    if k < smallest:
        smallest = k
print("smallest is",smallest)
    

    
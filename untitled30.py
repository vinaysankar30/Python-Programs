# -*- coding: utf-8 -*-
"""
) Write a Python program to input a list of n numbers. 
Calculate and display the average of numbers. 
Also display the cube of each value in the list. (5)
"""
c = []
n = int(input("enter the no of terms"))
for i in range(n):
    k = int(input("input number"))
    c.append(k)
sum = 0
for j in c:
    sum = sum + j
print(sum/n)
q = []
for f in c:
    t = f**3
    q.append(t)
print(q)
    
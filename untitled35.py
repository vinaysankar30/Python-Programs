# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 20:42:43 2018

@author: admin
"""

a = []
for i in range(int(input("enter range"))):
    b = []
    for j in range(1):
        name = input("enter name")
        score = float(input("enter marks"))
        b.append(name)
        b.append(score)
    a.append(b)
l = dict(a)
res = dict((v,k) for k,v in l.items())
print(res)
for i in res.keys():
    print(i)
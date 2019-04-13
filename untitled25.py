# -*- coding: utf-8 by Vinay -*-
"""
 Create a class person with attributes Name, age, 
 salary and a method display()for
showing the details. Create two 
instances of the class and call the method for 
"""
class Person:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def display(self):
        print("Name is ",self.name,"age is",self.age,"salary is",self.salary)
a = Person("Vinay",20,4500000000)
b = Person("x",30,100)
a.display()
b.display()
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 17:20:06 2022

@author: jianxuFX
"""


#get input

num=float(input("please enter a number:"))
if(num<0):
    print('negetive numbers are not allowed')
    exit()


g=float(input('please enter a nuber to start to guess:'))
if g<0:
    print('negetive numbers are not allowed')
    exit()

#the two numbers are not close enough 
while abs(g*g-num)>=0.01:
    g=(g+num/g)/2

#find the close enough number
print(str(round(g,3))+' '+'is the squre root of '+' '+str(num))


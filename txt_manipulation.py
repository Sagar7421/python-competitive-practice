# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:34:24 2020

@author: Soul
"""

f = open('train_list.txt', 'r')

g = open('new_train.txt', 'w')

s = f.readlines()

for i in s:
    tp = i.split('/')
    fs = tp[7]
    g.write(fs)
    
f.close()
g.close()
myString = f.readline()

a = myString.split('/')

name, desc = a[7].split('\t')
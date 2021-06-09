# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 15:28:11 2020

@author: Soul
"""

def oneHop(hArr, x, y):
    hops = tuple(((x-1, y), (x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1)))
    honey = 0
    l = len(hArr)
    m = len(hArr[0])
    for i, j in hops:
        if i < 0 or j < 0 or i >= l or j >= m:
            continue
        else:
            honey += hArr[i][j]
    
    return honey

def twoHop(hArr, x, y):
    hops2 = tuple(((x-2, y), (x-1, y+1), (x-1, y+2), (x, y+2), (x+1, y+2), (x+2, y+1), (x+2, y), (x+2, y-1), (x+1, y-2), (x, y-2), (x-1, y-2), (x-1, y-1)))
    honey2 = 0
    l = len(hArr)
    m = len(hArr[0])
    for i, j in hops2:
        if i < 0 or j < 0 or i >= l or j >= m:
            continue
        else:
            honey2 += hArr[i][j]
    
    return honey2

for _ in range(int(input())):
    N, M = map(int, input().split())
    N, M = int(N), int(M)
    hArr = []
    for _ in range(N):
        hArr.append(list(map(int, input().split())))

    for _ in range(int(input())):
        q, x, y = map(int, input().split())
        res = 0
        if q == 1:
            res = oneHop(hArr, x, y)
            print(res)
        else:
            res = twoHop(hArr, x, y)
            print(res)



#Testing Purpose
arr = [[1,1,2,3,4,5], [1,1,2,3,4,5], [1,1,2,3,4,5], [1,1,2,3,4,5], [1,1,2,3,4,5], [1,1,2,3,4,5]]

print(twoHop(arr, 2, 3))
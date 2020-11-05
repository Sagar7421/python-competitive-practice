# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 23:02:40 2020

@author: Soul
"""
# Write your code here
import copy

def checkSimi(arr, N):
    ans = False
    quad1, quad2, quad3, quad4 = [],[],[],[]
    if N % 2 != 0:
        modu = N//2
        for i in range(modu+1):
            if arr[i][modu] == arr[N-i-1][modu] and arr[modu][i] == arr[modu][N-1-i]:
                ans = True
            else:
                return False
        div = N//2
                
        #quads
        for i in range(div):
            quad1.append(arr[i][:div])
                
        for j in range(div):
            quad2.append(arr[j][div+1:])

        for k in range(div):
            quad3.append(arr[k+div+1][:div])

        for l in range(div):
            quad4.append(arr[l+div+1][div+1:])
                
        r_q3 = quad3.copy()
        r_q4 = quad4.copy()
        r_q2_q1 = copy.deepcopy(quad2)
        r_q3.reverse(), r_q4.reverse()
        for p in range(len(r_q2_q1)):
            r_q2_q1[p].reverse() 

        if quad1 == r_q2_q1 and quad1 == r_q3 and quad2 == r_q4:
            ans = True
        else:
            ans = False
        #Even ke liye                        
    else:
        div = int(N/2)
                
        #quads
        for i in range(0, div):
            quad1.append(arr[i][:div])
                
        for j in range(0, div):
            quad2.append(arr[j][div:])

        for k in range(0, div):
            quad3.append(arr[k+div][:div])

        for l in range(0, div):
            quad4.append(arr[l+div][div:])
                
        r_q3 = quad3.copy()
        r_q4 = quad4.copy()
        r_q2_q1 = copy.deepcopy(quad2)
        r_q3.reverse(), r_q4.reverse()
        for p in range(len(r_q2_q1)):
            r_q2_q1[p].reverse()     
        
        if (quad1 == r_q2_q1 and quad1 == r_q3) and quad2 == r_q4:
            ans = True
        else:
            ans = False


    return ans       


for _ in range(int(input())):
    N = int(input())
    arr = []
    for i in range(N):
        a = input()
        a = [int(j) for j in a]
        arr.append(a)
        
    res = checkSimi(arr, N)
    if res == True:
        print('YES')
    else:
        print('NO')
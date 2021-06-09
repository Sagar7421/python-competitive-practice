# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 16:02:59 2021

@author: Soul
"""

def leftShifting(binStr, N, K):
    tempStr = binStr 
    tempHigh = 0
    its = 0

    for times in range(N+1):
        curNum = int("".join(tempStr), 2)

        if curNum > tempHigh:
            tempHigh = curNum
            its = times
        
        tempStr = tempStr[1:] + tempStr[:1]
    
    newStart = binStr[its:] + binStr[:its]
    highString = binStr[its:] + binStr[:its]
    count = 0
    while(K>1):
        count += 1
        newStart = newStart[1:] + newStart[:1]

        if highString == newStart:
            K -= 1
            its += count
    
    return its
        

def rightShifting(binStr, N, K):
   pass


# Write your code here
for _ in range (int(input())):
    N, K = map(int, input().split())
    S = input()
    ls = list(S)
    
    itTimes = leftShifting(ls, N, K)
    print(itTimes)
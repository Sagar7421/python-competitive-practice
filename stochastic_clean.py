# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:51:47 2020

@author: Soul
"""

def nextMove(posr, posc, board):
    
    #finding dirty cell
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 'd':
                x = i
                y = j
                break
    
    #distance
    difV, difH = posr - x, posc - y
    if difV > 0:
        d_c = difV
    else:
        u_c = abs(difV)
    if difH > 0:
        r_c = difH
    else:
        l_c = abs(difH)
    
    
                
    
    
    print ""

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
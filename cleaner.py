# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        print("CLEAN")
    
    elif board[posr][posc] == 'b':
        if board[posr][posc+1] == 'd':
            #posc = posc + 1
            print("RIGHT")
            
        elif board[posr][posc-1] == 'd':
            #posc = posc - 1
            print("LEFT")
        elif board[posr+1][posc] == 'd':
            #posr = posr + 1
            print("DOWN")
        elif board[posr-1][posc] == 'd':
            #posr = posr - 1
            print("UP")
        elif board[posr][posc+1] == '-':
            for i in range(posc,len(board)):
                if board[posr][i] == 'd':
                    #posc = i
                    print("RIGHT")
                    break
        elif board[posr][posc-1] == '-':
            for j in range(posc,-1,-1):
                if board[posr][j] == 'd':
                    #posc = j
                    print("LEFT")
                    break
        else:
            #posr = posr + 1
            print("DOWN")
                
    

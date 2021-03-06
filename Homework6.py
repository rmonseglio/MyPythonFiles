# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 15:04:02 2021

@author: Coding.Troll(Richard Monseglio)
"""

rows = 5
columns = 5

def board(rows, columns):
    for row in range(rows):
        if row%2==0:
            for col in range(1,columns+1):
                if col%2==1:
                    if col != columns:
                        print(" ",end="")
                    else:
                        print(" ")
                else:
                    print("|",end="")
        else:
            print("-----")
    return True
            
print(board(rows, columns))


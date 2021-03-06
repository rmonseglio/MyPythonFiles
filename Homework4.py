# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:22:59 2021

@author: richa
"""



myUniqueList = []
myLeftovers = []
userInput = ''


    

    
def addList():
    userInput = ''
    while userInput != 'stop':
        userInput = input("Enter a unique word: ")
        myLeftovers.append(userInput)
        if userInput not in myUniqueList:
            myUniqueList.append(userInput)
            print(True)
        else:
            print(False)

        
run = addList()
  
print("My Unique List",str(myUniqueList))




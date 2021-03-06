# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 12:16:12 2021

@author: Coding.Troll(Richard Monseglio)
"""

num = 0

for num in range(100):
    prime = True
    if num%3 == 0 and num%5 == 0:
        print( "FizzBuzz")
        continue
    elif num%3 == 0:
        print( "Fizz")
        continue
    elif num%5 == 0:
        print( "Buzz")
        continue
    print(num)
    
    
            
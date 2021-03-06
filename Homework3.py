# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 16:57:46 2021

@author: richa
"""



def LogIn(UserName, UserPassword):
    UserName = "Richard"
    UserPassword = "123456"
    Password = False
    if UserName == "Richard" and UserPassword == str(123456):
        Password = True
    return Password

user = " "," "

User1 = LogIn(UserName=..., UserPassword=...)

print(User1)
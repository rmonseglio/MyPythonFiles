# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 21:22:53 2021

@author: richa
"""

def artist(name):
    name = "Highly Suspect"
    return name

def songTitle(title):
    title = "Bloodfeather"
    return title

def dateReleased(year):
    year = "2015"
    return year

def hasVideo():
    return True
    

a = " "
t = " "
y = " "


a = artist(name= "")
t = songTitle(title= "")
y = dateReleased(year= "")

print("Band Name: " + a)
print("Song Title: " + t)
print("Year of Song release: " + y)
print("This song has a video? ", hasVideo())

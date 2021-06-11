#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Feb 21 22:43:00 2021

@author: user
"""

#import random
import random

#user health
health = 50

#diffculty levels 
diffculty = 1

#convert float into a int()
check_health = int(random.randint(25,50) / diffculty)


health = health + check_health

#print the new value on the screen 
print(health)


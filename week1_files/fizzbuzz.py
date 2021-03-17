#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 12:21:30 2021

@author: giudittaparolini
"""


for x in range(1,101):
    if x%3 == 0 and x%5 == 0:
        print(x, "FizzBuzz")
    elif x%3 == 0:
        print(x, "Fizz")
    elif x%5 == 0:
        print(x, "Buzz")
        
        
        
def fizzbuzz(n):
    for x in range(1,n+1):
        if x%3 == 0 and x%5 == 0:
            print(x, "FizzBuzz")
        elif x%3 == 0:
            print(x, "Fizz")
        elif x%5 == 0:
            print(x, "Buzz")
    return

fizzbuzz (50)
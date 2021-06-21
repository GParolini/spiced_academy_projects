#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 15:14:18 2021

@author: giudittaparolini
"""
from customers_instances.py import Customer
#import numpy as np
#from numpy.random import choice
#import pandas as pd

# Creating a set of 20 customers
loc_list = ['dairy', 'drinks', 'fruit','spices']
customers = [Customer(Faker().name(), random.choice(loc_list))[i] for i in range (0,20)]
                      

print(customers)       


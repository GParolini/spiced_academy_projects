#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 15:14:18 2021

@author: giudittaparolini
"""
from customers_class import Customer
from faker import Faker
import numpy as np
from datetime import datetime, timedelta
import pandas as pd
import csv
import os

# Creating the customers (1000)
loc_list = ['dairy', 'drinks', 'fruit','spices']
customers = [Customer(Faker().name(), np.random.choice(loc_list)) for i in range (0, 1000)]

for customer in customers:
    print(customer.name, customer.state, customer.is_active())


# Simulation

if os.path.exists("simulation.csv"):
    os.remove("simulation.csv")

while len(customers)>0:
    lst_inactive_cust = []
    for customer in customers:
        times=pd.date_range("07:00:00","21:30:00",freq="3.0min").strftime("%H:%M:%S")
        timestamp=np.random.choice(times)
        with open('simulation.csv','a') as out:
            csv_out=csv.writer(out)
            csv_out.writerow([timestamp, customer.name, customer.state])
        for i in range (1,50,1):
            if customer.is_active() != True:
                lst_inactive_cust.append(customer)
                break
            else:
                customer.state = customer.next_state()
                timestamp=(datetime.strptime(timestamp,'%H:%M:%S')+timedelta(minutes=3)).time().strftime("%H:%M:%S")
                print(timestamp, customer.name, customer.state)
                with open('simulation.csv','a') as out:
                    csv_out=csv.writer(out)
                    csv_out.writerow([timestamp, customer.name, customer.state])


    for my_cust in lst_inactive_cust:
        customers.remove(my_cust)

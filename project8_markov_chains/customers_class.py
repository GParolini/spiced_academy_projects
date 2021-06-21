#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 15:14:18 2021

@author: giudittaparolini
"""
from faker import Faker
import numpy as np
from numpy.random import choice
import pandas as pd


class Customer:
    """
    a single customer that moves through the supermarket
    in a MCMC simulation
    """
    def __init__(self, name, state):
        self.name = name
        self.state = state
        self.trans_probs = pd.read_csv("transition_matrix.csv", index_col=0)


    def __repr__(self):
        return f'<Customer {self.name} in {self.state}>'


    def next_state(self):
        '''
        Propagates the customer to the next state.
        Returns nothing.
        '''
        loc_list = ['checkout','dairy', 'drinks', 'fruit','spices']
        initial_state = self.state
        weights = self.trans_probs.loc[initial_state].to_numpy().tolist()
        new_state = np.random.choice(loc_list,5, p=weights)[0]
        return new_state


    def is_active(self):
        """Returns True if the customer has not reached the checkout yet."""
        if self.state != 'checkout':
            return True

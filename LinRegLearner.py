'''===========================================================
    Linear Regression Learner Class does...
    
    Imports:
    numpy: Numerical analysis library
    pandas: Matrix data processor
    matplotlib.pyplot: Used for plotting data
============================================================'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import DataImport


class LinRegLearner:
    def __init__(self):
        continue
'''===========================================================
Training method takes in x and y (x can be multi-dimensional) &
it attempts to fit a line into it, tries to find an m and b
(self refers to the local instance of that variable)

The x_train being input into here are different features for
different stocks. The different dimensions can be represented
by different x indeces. x1_train _______,
x2_train_____,x3_train ______. This should be older data
represented in tabular format.

Features:

The y_train data is the prices of the stocks from the x_train
data.

Find a linear regression from Numpy or SciPy and stuff its
output into m and b
==========================================================='''
    def train(self,x,y):
        train_data = mid_prices[:10000]
        #self.m, self.b = favorite_lin_Reg(x,y)

'''===========================================================
x_text is passed into query method (x can be multi-dimensional)
and y predicted is computed.
==========================================================='''
    def query(x):
        #y = self.m * x + self.b
        #return y




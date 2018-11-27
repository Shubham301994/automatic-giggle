'''===========================================================
    Linear Regression Learner Class does...
    
    Imports:
    numpy: Numerical analysis library
    pandas: Matrix data processor
    matplotlib.pyplot: Used for plotting data
    DataImport: class from DataImport file
    MinMaxScaler: transforms features by scaling to given range
============================================================'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from DataImport import DataImport
from sklearn.preprocessing import MinMaxScaler

class LinRegLearner:
    #def __init__(self):
    #continue
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
        dataImport = DataImport()

        highDF=dataImport.pull_high('aapl','1/1/1970','31/12/2017')
        lowDF=dataImport.pull_low('aapl','1/1/1970','31/12/2017')
        highPrices = np.array(highDF.values)#obtains values only from DF
        lowPrices = np.array(lowDF.values)#obtains values only from DF
        
        #Find average of high and low prices
        self.medPrices=(highPrices+lowPrices)/2.0
        
        trainData = self.medPrices[:4600]#1st 4600 points to train
        testData = self.medPrices[4600:]#2nd 4600 points to test

        scaler = MinMaxScaler()#scales data to be within a region
        trainData = trainData.reshape(-1,1)#-1 is unknown num of rows+
    
        #Train the scaler with training and smooth data
        smoothingWindowSize = 1000
        '''Split data into sections. Since earlier stock data is closer to 0 & won't be
        relevant for training. So break into sections then normalize'''
        for di in range (0,4000,smoothingWindowSize):
            #scaler.fit Computes Min and Max
            scaler.fit(trainData[di:di+smoothingWindowSize,:])
            
            trainData[di:di+smoothingWindowSize,:] = scaler.transform(trainData[di:di+smoothingWindowSize,:])
        
            #Normalize last remaining data
        scaler.fit(trainData[di+smoothingWindowSize:,:])
        trainData[di+smoothingWindowSize:,:] = scaler.transform(trainData[di+smoothingWindowSize:,:])
        
        #Reshape train and test data
        trainData = trainData.reshape(-1)

        #DO Exponential Moving Average Smoothing
        #The data will have a smoother curve than the original noisy data
        ema = 0.0
        gamma = 0.1
        for ti in range(4600):
            ema = gamma * trainData[ti] + (1-gamma)*ema
            trainData[ti] = ema
        allMidData = np.concatenate([trainData,testData],axis=0)
        #self.m, self.b = favorite_lin_Reg(x,y)
        
        
        

    '''===========================================================
    x_text is passed into query method (x can be multi-dimensional)
    and y predicted is computed.
    ==========================================================='''
    def test(x):
        testData = testData.reshape(-1,1)#MOVE ME FROM HERE TO DIFFERENT FUNCTION
        testData = scaler.transform(testData.reshape(-1))#Do Not smooth out testData


        #y = self.m * x + self.b
        #return y

if __name__=='__main__':
    '''use this in every class in order to test them separately'''
    lrLearner = LinRegLearner()
    lrLearner.train(4,5)





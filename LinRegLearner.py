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
    #self.trainData
    '''===========================================================

    ==========================================================='''
    def medPriceCalc():
        '''
            Medium Price Calculation:
            pulls high & low price as a Data Frame from DataImport
            Converts to Numpy Array and extracts values
            calc averages of high & low prices, returns medPrices
        '''
        data = DataImport()
        highDF=data.pull_feat('ge','1/1/1962','27/11/2017','High')
        lowDF=data.pull_feat('ge','1/1/1962','27/11/2017','Low')
        highPrices = np.array(highDF.values)
        lowPrices = np.array(lowDF.values)
        
        medPrices=(highPrices+lowPrices)/2.0
        return medPrices
    
    def train(self):
        '''
            Raw Train data as a Numpy Array, 1st 7000 points
        '''
        medPrices = LinRegLearner.medPriceCalc()
        trainData = medPrices[:7000]
        return trainData
    
    def test(self):
        '''
            Raw Test data as a Numpy Array, 2nd 7000 points
        '''
        medPrices = LinRegLearner.medPriceCalc()
        testData = medPrices[7000:]
        return testData
        
    def scaling(self):
        '''
            scales train and test data to be within a region
        '''
        scaler = MinMaxScaler()
        trainData = LinRegLearner.train(self)
        testData = LinRegLearner.test(self)
        
        trainData = trainData.reshape(-1,1)#-1 is unknown num of rows+
        testData = testData.reshape(-1,1)

        #Train the scaler with training and smooth data
        smoothingWindowSize = 1625
        '''Split data into sections. Since earlier stock data is closer to 0 & won't be
            relevant for training. So break into sections then normalize'''
        for di in range (0,6500,smoothingWindowSize):
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
        for ti in range(6500):
            ema = gamma * trainData[ti] + (1-gamma)*ema
            trainData[ti] = ema

        testData = scaler.transform(testData).reshape(-1)#Do Not smooth out testData
        allMidData = np.concatenate([trainData,testData],axis=0)
        return allMidData

if __name__=='__main__':
    '''use this in every class in order to test them separately'''
    lrLearner = LinRegLearner()
    
    trainSet = lrLearner.train()
    testSet = lrLearner.test()
    scaling = lrLearner.scaling()
              
    print('Train:',trainSet)
    print('Test:',testSet)
    print('Scaled Mid Data:',scaling)
#lrLearner.eofSmoorhing(dataImport)





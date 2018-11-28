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
    def med_price():
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
    
    def train_data(self):
        '''
            Raw Train data as a Numpy Array, 1st 7000 points
        '''
        medPrices = LinRegLearner.med_price()
        trainData = medPrices[:7000]
        return trainData
    
    def test_data(self):
        '''
            Raw Test data as a Numpy Array, 2nd 7000 points
        '''
        medPrices = LinRegLearner.med_price()
        testData = medPrices[7000:]
        return testData
        
    def data_scaling(self):
        '''
            scales data to be within a region. Since older
            data tends to be closer to 0, it wont have much
            relevance for training. So data is broken into
            sections then its normalized
        '''
        scaler = MinMaxScaler()
        trainData = LinRegLearner.train_data(self)
        testData = LinRegLearner.test_data(self)
        
        #Ensures 2D array. -1 is unknown num of rows
        trainData = trainData.reshape(-1,1)
        testData = testData.reshape(-1,1)

        #number of points to analyze at a time
        smoothingWindowSize = 1625

        for di in range (0,6500,smoothingWindowSize):
            #Compute min and max to be used later for transform
            scaler.fit(trainData[di:di+smoothingWindowSize,:])
            
            #scaling of trainData based on a 0 - 1 range
            trainData[di:di+smoothingWindowSize,:] = scaler.transform(trainData[di:di+smoothingWindowSize,:])
    
        #Normalize the remaining data
        scaler.fit(trainData[di+smoothingWindowSize:,:])
        trainData[di+smoothingWindowSize:,:] = scaler.transform(trainData[di+smoothingWindowSize:,:])
        
        #Reshape train and test data
        trainData = trainData.reshape(-1)
        
        #Do Not smooth out testData
        testData = scaler.transform(testData).reshape(-1)

        #DO Exponential Moving Average Smoothing
        #The data will have a smoother curve than the original noisy data
        ema = 0.0
        gamma = 0.1
        for ti in range(7000):
            ema = gamma * trainData[ti] + (1-gamma)*ema
            trainData[ti] = ema

        allMidData = np.concatenate([trainData,testData],axis=0)
        return allMidData

if __name__=='__main__':
    '''use this in every class in order to test them separately'''
    lrLearner = LinRegLearner()
    
    trainSet = lrLearner.train_data()
    testSet = lrLearner.test_data()
    lrLearner.data_scaling()
              
#    print('Train:',trainSet)
#    print('Test:',testSet)
#    print('Scaled Mid Data:',data_scaling)
#lrLearner.eofSmoorhing(dataImport)





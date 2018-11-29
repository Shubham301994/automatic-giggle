'''===========================================================
    Imports:
    numpy: Numerical analysis of large data sets
    pandas: Matrix data processor
    DataImport: class from DataImport file
    MinMaxScaler: transforms features by scaling to given range
    datetime: used to create arrays of dates and strip time
============================================================'''
import numpy as np
import pandas as pd
from DataImport import DataImport
from sklearn.preprocessing import MinMaxScaler
import datetime as dt

class LinRegLearner:
    '''===========================================================
    This module computes the mid_price, then divides it into
    training and testing data. It scales and fits the train and
    test data accordingly. Also, smooths out train data to remove
    noise. This returns a tuple of scaled/smoothed trainData &
    scaled testData. This trainData and testData is combined.
    Dates are extracted from a dataFrame of stock data, it is used
    to compute a Standard Average and an Exponential Moving Average
    ==========================================================='''
    def mid_price(self,ticker,start,end):
        '''
            Medium Price Calculation:
            pulls high & low price as a Data Frame from DataImport
            Converts to Numpy Array and extracts values
            calc averages of high & low prices, returns medPrices
        '''
        data = DataImport()
        highDF=data.pull_feat(ticker,start,end,'High')
        lowDF=data.pull_feat(ticker,start,end,'Low')
        highPrices = np.array(highDF.values)
        lowPrices = np.array(lowDF.values)
        
        self.medPrices=(highPrices+lowPrices)/2.0
        return self.medPrices
    
    def train_data(self,ticker,start,end):
        '''
            Raw Train data as a Numpy Array, 1st 7000 points
        '''
        self.medPrices = LinRegLearner.mid_price(self,ticker,start,end)
        trainData = self.medPrices[:7000]
        return trainData
    
    def test_data(self,ticker,start,end):
        '''
            Raw Test data as a Numpy Array, 2nd 7000 points
        '''
        ticker = 'ge'
        start = '1/1/1962'
        end = '28/11/2018'
        self.medPrices = LinRegLearner.mid_price(self,ticker,start,end)
        testData = self.medPrices[7000:]
        return testData
        
    def data_scaling(self,rawTrainData,rawTestData):
        '''
            scales data to be within a region. Since older
            data tends to be closer to 0, it wont have much
            relevance for training. Train Data is broken into
            sections it is then normalized.
        '''
        scaler = MinMaxScaler()#Instantiate the MinMaxScaler
        
        '''Ensures 2D array. When using -1 the value is
        inferred from the length of array & remaining dimensions.'''
        trainData = rawTrainData.reshape(-1,1)
        testData = rawTestData.reshape(-1,1)

        #number of points to analyze at a time
        smoothWindowSize = 1625
        for di in range (0,6500,smoothWindowSize):
            #Compute min and max to be used later for transform
            scaler.fit(trainData[di:di+smoothWindowSize,:])
            
            #scaling of trainData based on a 0 - 1 range
            trainData[di:di+smoothWindowSize,:] = scaler.transform(trainData[di:di+smoothWindowSize,:])
    
        #Normalize the remaining points
        scaler.fit(trainData[di+smoothWindowSize:,:])
        trainData[di+smoothWindowSize:,:] = scaler.transform(trainData[di+smoothWindowSize:,:])
        
        #Reshape trainData -1 means unknown size
        trainData = trainData.reshape(-1)
        #Do Not smooth out testData, but scale it on 0 - 1 range
        testData = scaler.transform(testData).reshape(-1)

        '''Exponential Moving Average Smoothing provides smoother Data
        that has smoother curve than the original noisy data'''
        ema = 0.0
        gamma = 0.1
        for ti in range(7000):
            ema = gamma * trainData[ti] + (1-gamma)*ema
            trainData[ti] = ema
                
        #Returns a tuple of scaled/smoothed trainData & scaled testData
        return trainData,testData
    
    def concat_train_test(self,trainData,testData):
        '''
            Combines trainData & testData, which represents mid_price()
            after scaling and smoothing
        '''
        trainTestMid = np.concatenate([trainData,testData],axis=0)
        return trainTestMid
    
    def extract_dates(self):
        '''
            Pulls DataFrame for dates specified, which contain
            7000 points of data. The indexes of df are the dates
            themselves, so reset_index treats the dates as data
            that is part of the dataFrame. DF.columns[0] extracts
            the dates and returns it as a pandas dataFrame
        '''
        data = DataImport()
        DF = data.pull_DF('ge','1/1/1962','10/30/1989')
        DF = DF.reset_index()
        dates = DF[DF.columns[0]]
        return dates
    
    def std_avg(self,scaledTrain,dates):
        '''
            Calculates a standard average of historical stock data
            that was previously observed. This calculated average is
            the predicted future stock market prices within a fixed
            window size. windowSize represents a window of 100 points
            of data. The prediction of a day ahead is the average of
            all the stock prices 100 days previous to the current day.
        '''
        data = DataImport()
        windowSize = 100
        N = scaledTrain.size
        stdAvgPredict = []#array of standard Average Predictions
        stdAvgX = []#array of the dates being analuzed
        mseErrors = []#array of Mean Squared Error(MSE)

        for idx in range(windowSize,N):
            if idx >= N:
                #Strips off time and adds 1 day using timedelta
                date = dt.datetime.strptime(str(date),'%Y-%m-%d  %H:%M:%S').date() + dt.timedelta(days=1)
            else:
                date = dt.datetime.strptime(str(dates[idx]),'%Y-%m-%d  %H:%M:%S').date()
            
            #Calculates average of previous stock data within a windowSize
            mean = np.mean(scaledTrain[idx-windowSize:idx])
            stdAvgPredict.append(mean)
            
            '''Calculates MSE, by taking the squared error b/w the actual value one point
            ahead and the predicted value'''
            mseError = (stdAvgPredict[-1]-scaledTrain[idx])**2
            
            mseErrors.append(mseError)
            stdAvgX.append(date)

        #Average of all errors
        meanError = np.mean(mseErrors)
        mse = 0.5*meanError
        
        #.5f uses 5 point precision
        print('MSE error for standard averaging: %.5f'%(mse))
        return stdAvgPredict

    def exp_moving_avg(self,scaledTrain):
        '''
            Calculates an Exponential Moving Average (EAM) maintained over
            time of historical stock data. decay decides how relevant is
            the most current prediction towards the EMA. In our case, it will
            be 0.5.
        '''
        windowSize = 100
        N = scaledTrain.size
        runAvgPredict = []#array of running Average Predictions
        emaMSE = []#MSE array of EMA
        runMean = 0.0
        runAvgPredict.append(runMean)
        decay = 0.5

        for predict in range(1,N):
            #Calculates the running average
            runMean = decay * runMean + (1.0-decay)*scaledTrain[predict-1]
            runAvgPredict.append(runMean)
            
            #Calculates the error for the running average
            emaError = (runAvgPredict[-1]-scaledTrain[predict])**2
            emaMSE.append(emaError)

        print('MSE error for EMA averaging: %.5f'%(0.5*np.mean(emaMSE)))

if __name__=='__main__':
    '''Used to test this class separately'''
    lrLearner = LinRegLearner()
    ticker = 'ge'
    start = '1/1/1962'
    end = '28/11/2018'
    
    trainSet = lrLearner.train_data(ticker,start,end)
    testSet = lrLearner.test_data(ticker,start,end)
    scaledTrainTest = lrLearner.data_scaling(trainSet,testSet)
    
    scaledTrain = scaledTrainTest[0]
    scaledTest = scaledTrainTest[1]

    dates = lrLearner.extract_dates()
    
    lrLearner.std_avg(scaledTrain,dates)
    lrLearner.exp_moving_avg(scaledTrain)
              






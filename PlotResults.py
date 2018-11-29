import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import numpy as np
from DataImport import DataImport
from LinRegLearner import LinRegLearner

class PlotResults:
    '''===========================================================
        This module generates 3 plots. The first plot is the raw
        stock medium price for a the full range of start to end.
        The second generated plot overlays the actual stock price
        and the predicted stock price using a standard mean
        algorithm. The third plot overlays the actual stock price
        and the predicted stock price when calculating the
        exponential moving average
    ==========================================================='''
    def rawTrain_rawTest_plot(self):
        ticker = 'ge'
        start = '1/1/1962'
        end = '28/11/2018'
        data = DataImport()
        DF = data.pull_DF(ticker,start,end)
        DF = DF.reset_index()
        datesOnly = DF[DF.columns[0]]
        datesAlone = []
        
        for i in range(0,datesOnly.size):
            date = dt.datetime.strptime(str(datesOnly[i]),'%Y-%m-%d  %H:%M:%S').date()
            datesAlone.append(date)
        
        dates = np.array(datesAlone)
        
        lrLearner = LinRegLearner()
        medPrices = lrLearner.mid_price(ticker,start,end)
        plt.figure(figsize = (14,7))
        plt.plot(range(DF.shape[0]),medPrices)
        
        plt.xticks(range(0,len(datesAlone),500),dates[::500],rotation=45)
        plt.xlabel('Date',fontsize=9)
        plt.ylabel('Mid Price',fontsize=9)
        plt.show()

    def std_avg_plot(self):
        
        ticker = 'ge'
        start = '1/1/1962'
        end = '28/11/2018'
        
        data = DataImport()

        
        lrLearner = LinRegLearner()
        trainData=lrLearner.train_data(ticker,start,end)
        testData=lrLearner.test_data(ticker,start,end)
        trainTestMid = lrLearner.concat_train_test(trainData,testData)
        
        DF = data.pull_DF(ticker,start,end)
        DF = DF.reset_index()
        datesOnly = DF[DF.columns[0]]
        datesAlone = []
        
        dts = lrLearner.extract_dates()
        
        for i in range(0,datesOnly.size):
            date = dt.datetime.strptime(str(datesOnly[i]),'%Y-%m-%d  %H:%M:%S').date()
            datesAlone.append(date)
        
        dates = np.array(datesAlone)
        
        scaledTrainTest = lrLearner.data_scaling(trainData,testData)
        scaledTrain = scaledTrainTest[0]
        
        stdAvgPredict = lrLearner.std_avg(scaledTrain,dts)
        #print(stdAvgPredict)
        
        plt.figure(figsize = (14,7))
        plt.plot(range(7000),scaledTrain[:7000],color='b',label='True')
        plt.plot(range(100,7000),stdAvgPredict,color='orange',label='Prediction')
        #plt.xticks(range(0,len(datesAlone),500),dates[::500],rotation=45)
        plt.xlabel('Date')
        plt.ylabel('Mid Price')
        plt.legend(fontsize=18)
        plt.show()


if __name__=='__main__':
    '''use this in every class in order to test them separately'''
    
    plot = PlotResults()
    #plot.rawTrain_rawTest_plot()
    plot.std_avg_plot()

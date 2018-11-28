'''
==============================================================================
This module Imports Adjusted Close Prices for a ticker calculates a moving
average, standard, sets an upper band and lower band. This data is all plotted

Use this data to have an algorithm decide when to sell or buy stocks based on
an upper and lower bands.

To Do:
Create another module that takes this data and uses functions from Robinhood
API that makes transactions
==============================================================================
'''
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt

class DataImport:

    def pull_feat(self,ticker,start,end,feat):
        '''
            Uses pandas_datareader to pull Adjusted Close price for a
            ticker, from start date, to end date. Returns a Pandas DF of
            AdjCloseDF data. Adj Close is the stock's amdended closing price
            on any given day of trading to include distributions and corporate
            actions that occured at any time before the next day's open. Used
            for examining historical returns
        '''
        #These should be imported from main class
        self.ticker = ticker
        self.start = start
        self.end = end
        
        self.feature = web.DataReader(self.ticker,data_source='yahoo',start = self.start,end = self.end)[feat]
        self.featDF = pd.DataFrame(self.feature)#Create the pandas Data Frame
        return self.featDF
    
    def calcs(self,fb):
        '''
            Takes the Adjusted Close Price
        '''
        fb['30 Day MA'] = fb['Adj Close'].rolling(window=20).mean()
        fb['30 Day STD'] = fb['Adj Close'].rolling(window=20).std()
        fb['Upper Band'] = fb['30 Day MA'] + (fb['30 Day STD'] * 2)
        fb['Lower Band'] = fb['30 Day MA'] - (fb['30 Day STD'] * 2)
    

if __name__=='__main__':
    '''use this in every class in order to test them separately'''
    
    dataImport = DataImport()
    fb = dataImport.pull_feat('ge','1/2/1962', '27/11/2018','High')
    print(fb.shape)

#dataImport.calcs(fb)






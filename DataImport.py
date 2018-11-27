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

    def pull_adj_close(self,ticker,start,end):
        '''
            Uses pandas_datareader to pull Adjusted Close price for a
            ticker, from start date, to end date. Returns a Pandas DF of
            AdjCloseDF data. Adj Close is the stock's amdended closing price
            on any given day of trading to include distributions and corporate
            actions that occured at any time before the next day's open. Used
            for examining historical returns
        '''
        self.ticker = ticker
        self.start = start
        self.end = end
        
        self.adjClose = web.DataReader(self.ticker,data_source='yahoo',start = self.start,end = self.end)['Adj Close']
        self.AdjCloseDF = pd.DataFrame(self.adjClose)#Create the pandas Data Frame
        return self.AdjCloseDF
    
    def pull_high(self,ticker,start,end):
        self.ticker = ticker
        self.start = start
        self.end = end
        
        self.high = web.DataReader(self.ticker,data_source='yahoo',start = self.start,end = self.end)['High']
        self.highDF = pd.DataFrame(self.high)#Create the pandas Data Frame
        print(self.highDF.shape)
        return self.highDF
    
    def pull_low(self,ticker,start,end):
        self.ticker = ticker
        self.start = start
        self.end = end
        
        self.high = web.DataReader(self.ticker,data_source='yahoo',start = self.start,end = self.end)['Low']
        self.lowDF = pd.DataFrame(self.high)#Create the pandas Data Frame
        return self.lowDF
    
    
    def calcs(self,fb):
        '''
            Takes the Adjusted Close Price
        '''
        fb['30 Day MA'] = fb['Adj Close'].rolling(window=20).mean()
        fb['30 Day STD'] = fb['Adj Close'].rolling(window=20).std()
        fb['Upper Band'] = fb['30 Day MA'] + (fb['30 Day STD'] * 2)
        fb['Lower Band'] = fb['30 Day MA'] - (fb['30 Day STD'] * 2)
    
    def bollinger_plot(self,fb):
        '''
            Takes the Adjusted Close Price
        '''
        fb[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
        plt.title('30 Day Bollinger Band for Facebook')
        plt.ylabel('Price (USD)')
        plt.show();

if __name__=='__main__':
    '''use this in every class in order to test them separately'''
    
    dataImport = DataImport()
    fb = dataImport.pull_adj_close('fb','1/1/2017', '31/12/2017')
    dataImport.calcs(fb)
    dataImport.bollinger_plot(fb)

    high = dataImport.pull_high('aapl','1/1/1970', '31/12/2017')





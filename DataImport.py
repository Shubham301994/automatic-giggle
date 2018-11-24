import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt

class DataImport:

    def pull_adj_close(self,ticker,start,end):
        '''
            Uses pandas_datareader to pull Adjusted Close data for a specific
            ticker, from a start date, to an end date. Returns a Pandas
            DataFrame of AdjustedClose data.
        '''
        self.ticker = ticker
        self.start = start
        self.end = end
        
        self.info = web.DataReader(self.ticker,data_source='yahoo',start = self.start,end = self.end)['Adj Close']
        self.AdjCloseDF = pd.DataFrame(self.info)#Create the pandas Data Frame
        return self.AdjCloseDF
    
    def calcs(self,fb):
        fb['30 Day MA'] = fb['Adj Close'].rolling(window=20).mean()
        fb['30 Day STD'] = fb['Adj Close'].rolling(window=20).std()
        fb['Upper Band'] = fb['30 Day MA'] + (fb['30 Day STD'] * 2)
        fb['Lower Band'] = fb['30 Day MA'] - (fb['30 Day STD'] * 2)

    def bollinger_plot(self,fb):
        fb[['Adj Close', '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
        plt.title('30 Day Bollinger Band for Facebook')
        plt.ylabel('Price (USD)')
        plt.show();

#use this in every class in order to test them separately
if __name__=='__main__':
    
    dataImport = DataImport()
    fb = dataImport.pull_adj_close('fb','1/1/2017', '31/12/2017')
    dataImport.calcs(fb)
    dataImport.bollinger_plot(fb)





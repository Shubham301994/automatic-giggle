import pandas as pd
from pandas_datareader import data as web

class DataImport:
    '''==============================================================================
        This module is used for importing stock data using the Pandas Data Reader
        which utilizing Yahoo Finnance database for historical stock data. Specific
        features can be imported as well as a full set of data. 
    =============================================================================='''
    def pull_feat(self,ticker,start,end,feat):
        '''
            Uses pandas_datareader to pull a feature for a ticker (ie. GOOG, AAPL, GE)
            from a start date to an end date. A feature can be Open Price, High Price, Low
            Price, Closing Price, Adj Close Price, and Volume. Returns a Pandas DF. These
            are all defined in the main application TradingWiz.
        '''
        self.feature = web.DataReader(ticker,data_source='yahoo',start=start,end=end)[feat]
        self.featDF = pd.DataFrame(self.feature)
        return self.featDF
    
    def pull_DF(self,ticker,start,end):
        '''
            Uses pandas_datareader to pull a full data frame that contains all features.
            Returns a Pandas DF containing all features.
        '''
        self.data = web.DataReader(ticker,data_source='yahoo',start=start,end=end)
        self.DF = pd.DataFrame(self.data)
        return self.DF

if __name__=='__main__':
    '''Used to test this class separately'''
    dataImport = DataImport()
    ge = dataImport.pull_DF('ge','1/2/1962', '27/11/2018')
    print(ge.shape)

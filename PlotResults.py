from DataImport import DataImport

class PlotResults:
    def bollinger_plot(self,fb,feat):
        #Need to pass in ticker,start,end in to here from TradingWiz
        #That way plotting can be generalized
        dataImport = DataImport()
        aapl=dataImport.pull_feat('aapl','1/1/1970','31/12/2017',feat)
        dataImport.calcs(

        '''
            Takes the Adjusted Close Price
            '''
        fb[[feat, '30 Day MA', 'Upper Band', 'Lower Band']].plot(figsize=(12,6))
        plt.title('30 Day Bollinger Band for Facebook')
        plt.ylabel('Price (USD)')
        plt.show();

if __name__=='__main__':
    '''use this in every class in order to test them separately'''
    
    dataImport.bollinger_plot(fb,'Adj Close')

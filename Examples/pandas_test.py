import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data_x = np.linspace(1.0,10.0,100)[:,np.newaxis]
#data_y = np.sin(data_x)+0.1*np.power(data_x,2)+0.5*np.random.randn(100,1)
#
##normalization of data, it helps in keeping the algorithm numerically stable
#data_x /= np.max(data_x)

#def get_max_close(symbol):
#    '''Returns the maximum closing value for stock indicated by symbol
#    Data is stored in AAPL.csv and IBM.csv
#        '''
#
#    df = pd.read_csv('{}.csv'.format(symbol))#load CSV file into a pandas data frame
#    return df['Close'].max

def test_run():
    df = pd.read_csv('AAPL.csv')
    print (df[['Adj Close','Close']])
    df[['Adj Close','Close']].plot()
    plt.show()

#    for symbol in ['AAPL','IBM']: This can be used 
#        print('Max close')
#        print(symbol,get_max_close(symbol))

if __name__=="__main__":
    test_run()



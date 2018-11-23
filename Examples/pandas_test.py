import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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



from DataImport import DataImport
from LinRegLearner import LinRegLearner


if __name__=='__main__':
    '''Main method to call funcs from other modules'''
    ticker = 'fb'
    start = '1/1/2017'
    end = '31/12/2017'
    feat = 'High
    
    dataImport = DataImport()
    LinRegLearner = LinRegLearner()
    fb = dataImport.pull_feat(ticker,start,end,feat)

    LinRegLearner.train(dataImport):


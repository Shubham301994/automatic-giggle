from LinRegLearner import LinRegLearner
'''===========================================================
    TradingWiz module calls the Learning module to predict
    prices of stocks using a Standard Average algorithm and an
    Exponential Moving Average. This main module feeds data to
    Plotting module to display the graphs for each of the
    training algorithms overlayed with the medium data
==========================================================='''
ticker = 'ge'
start = '1/1/1962'
end = '28/11/2018'

lrLearner = LinRegLearner()
trainData = lrLearner.train_data(ticker,start,end)#obtain trainData
testData = lrLearner.test_data(ticker,start,end)#obtain testData


#Obtain scaled train and test data concatenated
scaledTrainTest = lrLearner.data_scaling(trainData,testData)
scaledTrain = scaledTrainTest[0]
scaledTest = scaledTrainTest[1]

dates = lrLearner.extract_dates()
lrLearner.std_avg(scaledTrain,dates)
lrLearner.exp_moving_avg(scaledTrain)





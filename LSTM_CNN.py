import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM

class lstm:
    def __init__(self):
        df=pd.read_csv("/home/bigpenguin/Downloads/BTC-USD.csv")
        # df.drop('Open',axis=1,inplace=True)
        # df.drop('High',axis=1,inplace=True)
        # df.drop('Low',axis=1,inplace=True)
        # df.drop('Return',axis=1,inplace=True)
        # df.drop('Vol.',axis=1,inplace=True)
        # df.drop('Change %',axis=1,inplace=True)

        df=df.iloc[:,4:5]
        df=df.values

        scale=MinMaxScaler(feature_range=(0,1))
        df=scale.fit_transform(df)
        df=scale.fit_transform(df)
        xtrain=df[0:366]
        ytrain=df[1:367]

        xtrain=np.reshape(xtrain,(366,1,1))

        regressor = Sequential()

        #Adding the input layer and the LSTM layer
        regressor.add(LSTM(units = 4, activation = 'tanh', input_shape = (None, 1)))
        #Adding the output layer
        regressor.add(Dense(units = 1))
        #Compiling the Recurrent Neural Network
        regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
        #Fitting the Recurrent Neural Network [epoches is a kindoff number of iteration]
        regressor.fit(xtrain, xtrain, batch_size = 32, epochs = 200)

        test_df=pd.read_excel("/home/bigpenguin/Downloads/bitcoin_db.xlsx")
        test_df=test_df.iloc[:,1:2]

        ac_price=test_df.values
        inputs=ac_price
        inputs=scale.fit_transform(inputs)

        inputs = np.reshape(inputs, (3642, 1, 1))

        predict = regressor.predict(inputs)
        predict = scale.inverse_transform(predict)

        plt.plot(ac_price, color = 'red', label = 'Real BTC Value')
        plt.plot(predict, color = 'blue', label = 'Predicted BTC Value')
        plt.title('BTC Value Prediction')
        plt.xlabel('Days')
        plt.ylabel('BTC Value')
        plt.legend()
        plt.show()
        


if __name__=='__main__':
    obj=lstm()


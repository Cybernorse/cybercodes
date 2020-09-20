import pandas as pd
import numpy as np   
import matplotlib.pyplot as plt 
from sklearn.tree import DecisionTreeRegressor  
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score,auc,accuracy_score,average_precision_score,f1_score
class DTR:
    def __init__(self):
        df=pd.read_excel("/home/bigpenguin/Downloads/bitcoin_db.xlsx")
        df.drop('Open',axis=1,inplace=True)
        df.drop('High',axis=1,inplace=True)
        df.drop('Low',axis=1,inplace=True)
        df.drop('Return',axis=1,inplace=True)
        df.drop('Vol.',axis=1,inplace=True)
        df.drop('Change %',axis=1,inplace=True)
        

        df.drop(['Date'],1,inplace=True)

        prediction_days=60

        df['Prediction'] = df[['Price']].shift(-prediction_days)        
        
        x = np.array(df.drop(['Prediction'],1))    
        
        x = x[:len(df)-prediction_days] 
        # print(x)
        y = np.array(df['Prediction'])
        # Get all the values except last 'n' rows
        y = y[:-prediction_days]
        # print(y)

        from sklearn.model_selection import train_test_split
        xtrain, xtest, ytrain, ytest = train_test_split(x,y, test_size = 0.2)
        # set the predictionDays array equal to last 60 rows from the original data set
        predictiondays_array = np.array(df.drop(['Prediction'],1))[-prediction_days:]
        # print(predictiondays_array)

        # from sklearn.svm import SVR
        from sklearn.tree import DecisionTreeRegressor
        # Create and Train the Support Vector Machine (Regression) using radial basis function
        svr_rbf = DecisionTreeRegressor(random_state=0)
        svr_rbf.fit(xtrain, ytrain)

        svm_prediction = svr_rbf.predict(xtest)
        ys=[]
        for i in df['Price']:
            ys.append(i)
        
        print(roc_auc_score(df['Price'].values,svm_prediction))
        # print(xtest,ytest)
        # predict_days=svr_rbf.predict(predictiondays_array)

        # plt.scatter(x, y, color = 'red',label='Actual price',)
        # plt.scatter(predictiondays_array, predict_days, color = 'blue',label="Predicted price(Next 60 days)")
        # plt.legend(loc='upper right')
        # plt.show()

class LR:
    def __init__(self):
        df=pd.read_csv("/home/bigpenguin/Downloads/BTC-USD.csv")
        # df.drop('Open',axis=1,inplace=True)
        # df.drop('High',axis=1,inplace=True)
        # df.drop('Low',axis=1,inplace=True)
        df.drop('Date',axis=1,inplace=True)
        df.drop('Adj Close',axis=1,inplace=True)
        df.drop('Volume',axis=1,inplace=True)
        
        prediction_days=30

        X=df[['Open','High','Low']]
        Y=df['Close']

        x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=1/3,random_state=1)

        from sklearn.linear_model import LinearRegression
        regressor=LinearRegression()
        regressor.fit(x_train,y_train)

        test_predict=regressor.predict(x_test)
        # print(x_test,y_test)
        # plt.scatter(x_test, y_test, color = 'red')
        plt.plot(x_test, regressor.predict(x_test), color = 'blue')
        # plt.xlabel('Dates')
        # plt.ylabel('Prices')
        plt.show()

class svm:
    def __init__(self):
        df=pd.read_excel("/home/bigpenguin/Downloads/bitcoin_db.xlsx")
        df.drop('Open',axis=1,inplace=True)
        df.drop('High',axis=1,inplace=True)
        df.drop('Low',axis=1,inplace=True)
        df.drop('Return',axis=1,inplace=True)
        df.drop('Vol.',axis=1,inplace=True)
        df.drop('Change %',axis=1,inplace=True)
        

        df.drop(['Date'],1,inplace=True)

        prediction_days=60

        df['Prediction'] = df[['Price']].shift(-prediction_days)        
        
        x = np.array(df.drop(['Prediction'],1))    
        
        x = x[:len(df)-prediction_days] 
        # print(x)
        y = np.array(df['Prediction'])
        # Get all the values except last 'n' rows
        y = y[:-prediction_days]
        # print(y)

        from sklearn.model_selection import train_test_split
        xtrain, xtest, ytrain, ytest = train_test_split(x,y, test_size = 0.2)
        # set the predictionDays array equal to last 60 rows from the original data set
        predictiondays_array = np.array(df.drop(['Prediction'],1))[-prediction_days:]
        # print(predictiondays_array)

        from sklearn.svm import SVR
        # Create and Train the Support Vector Machine (Regression) using radial basis function
        svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.00001)
        svr_rbf.fit(xtrain, ytrain)

        svm_prediction = svr_rbf.predict(xtest)
        print(svr_rbf.score(xtest,ytest))
        predict_days=svr_rbf.predict(predictiondays_array)

        plt.scatter(x, y, color = 'red',label='Actual price',)
        plt.scatter(predictiondays_array, predict_days, color = 'blue',label="Predicted price(Next 60 days)")
        plt.legend(loc='upper right')
        plt.show()

if __name__=='__main__':
    obj=DTR()
    # obj=LR()
    # obj=svm()
    
        

from fbprophet import Prophet
import pandas as pd
import numpy as np

class bitcoin_predictions:
    def __init__(self):
        df=pd.read_csv("/home/bigpenguin/Downloads/BTC-USD.csv")
        df.drop('Open',axis=1,inplace=True)
        df.drop('High',axis=1,inplace=True)
        df.drop('Low',axis=1,inplace=True)
        df.drop('Adj Close',axis=1,inplace=True)
        df.drop('Volume',axis=1,inplace=True)
        # print(df.head())
        df.rename(columns={'Date': 'ds', 'Close': 'y'},inplace=True)

        df['y']=np.log(df['y'])

        m=Prophet(daily_seasonality=True,interval_width=0.95)
        m.fit(df)

        future=m.make_future_dataframe(periods=60,freq='D')
        future.tail()

        pred=m.predict(future)
        pred[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

        fig=m.plot(pred)
        fig.savefig('/home/bigpenguin/01_fbprophet_getting_started-02.png')
        
        
if __name__=="__main__":
    predict_obj=bitcoin_predictions()
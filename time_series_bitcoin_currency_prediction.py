from fbprophet import Prophet
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error,roc_auc_score,auc,accuracy_score,matthews_corrcoef
class bitcoin_predictions:
    def __init__(self):
        df=pd.read_excel("/home/bigpenguin/Downloads/bitcoin_db.xlsx")
        # df.drop('Total Volume',axis=1,inplace=True)
        df.drop('Open',axis=1,inplace=True)
        df.drop('High',axis=1,inplace=True)
        df.drop('Low',axis=1,inplace=True)
        df.drop('Return',axis=1,inplace=True)
        df.drop('Vol.',axis=1,inplace=True)
        df.drop('Change %',axis=1,inplace=True)
        # print(df.head())
        
        df.rename(columns={'Date': 'ds', 'Price': 'y'},inplace=True)
        
        df['y']=np.log(df['y'])

        m=Prophet( daily_seasonality=True,interval_width=0.95)
        m.fit(df)

        future=m.make_future_dataframe(periods=720,include_history=True)
        future.tail()

        pred=m.predict(future)
    
        pred[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
        
        print(len(pred['yhat'][:3642]))
        

        # print((sum(pred['yhat'])-sum(df['y']))/sum(df['y']))
        # fig=m.plot(pred)
        # fig=m.plot_components(pred)
        # fig.savefig('/home/bigpenguin/01_fbprophet_getting_started-03.png')
        
        
if __name__=="__main__":
    predict_obj=bitcoin_predictions()


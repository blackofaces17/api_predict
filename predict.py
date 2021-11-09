import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA
import warnings
import json

def predictions():
    
       

    df_energy=pd.read_csv('dataproject.csv')

    df_energy.columns=["Time","InsertTime","Status","Power Factor","Energy","Voltage"]


    df_energy= df_energy.drop(['Time','Status','Power Factor','Voltage'], axis = 1)

    df_energy['InsertTime'] = pd.to_datetime(df_energy['InsertTime'])

    df_energy['Date'] = df_energy['InsertTime'].dt.date

    df_energy=df_energy.groupby('Date', as_index=False).agg({"Energy": "mean"})

    df_energy.set_index('Date',inplace=True)

    model_arima=ARIMA(df_energy,order=(3,1,2))
    model_arima_fit=model_arima.fit()
    warnings.filterwarnings("ignore")

    start1=1
    end1=len(df_energy)
    predictions=model_arima_fit.predict(start=start1,end=end1,typ="levels")
    


    y = json.loads(json.dumps(predictions.T.to_dict()))
    return y 

import pandas as pd
import numpy as np
import json

def first_graph_return():
    df_energy=pd.read_csv('dataproject.csv')
    df_energy.columns=["Time","InsertTime","Status","Power Factor","Energy","Voltage"]
    df_energy= df_energy.drop(['Time','Status','Power Factor','Voltage'], axis = 1)
    df_energy['InsertTime'] = pd.to_datetime(df_energy['InsertTime'])
    df_energy['Date'] = df_energy['InsertTime'].dt.date
    df_energy=df_energy.groupby('Date', as_index=False).agg({"Energy": "mean"})
    df_energy.set_index('Date',inplace=True)
    li = []
    for i in df_energy.index:
        li.append(str(i))
    x = json.loads(json.dumps(df_energy.to_json()))
    x = json.loads(x)
    new_x = x['Energy']
    new_li = {}
    for i,k in enumerate(new_x):
        new_li[li[i]]= new_x[k]
    print(new_li)
    return new_li


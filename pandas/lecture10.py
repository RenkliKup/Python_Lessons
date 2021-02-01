import pandas as pd
import numpy as np
data=pd.read_csv("nba.csv")
data.dropna(inplace=True)
data["Name"]=data["Name"].str.upper()
data["Name"]=data["Name"].str.lower()
data["index"]=data["Name"].str.find("a")
result=data["Name"].str.contains("jordan")
data["Team"]=data["Team"].str.replace(" ","-")
data[["FirstName","LastName"]]=data["Name"].loc[data["Name"].str.split().str.len()==2].str.split(expand=True)

print(data.head())
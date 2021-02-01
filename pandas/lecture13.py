import pandas as pd
import numpy as np

data=pd.read_csv("nba.csv")

df=pd.DataFrame(data)
result=df.head(10)
result=len(df.index)#kayıt sayısı
result=df["Salary"].mean()
result=df["Salary"].max()
result=df[df["Salary"]==df["Salary"].max()].max()["Name"]
result=df[(df["Age"]>=20) & (df["Age"]<=25)][["Name","Team","Age"]].sort_values("Age",ascending=False)
result=df[df["Name"]=="John Holland"][["Name","Team"]]
result=df.groupby("Team").mean()["Salary"]
result=len(df.groupby("Team"))
result=df["Team"].value_counts()
print(result)
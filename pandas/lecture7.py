import pandas as pd
import numpy as np

df=pd.read_csv("imdb.csv")
result=df.columns
result=df.dtypes
result=type(df)
result=df.head(10)
result=df.tail()
result=df.tail(10)
result=df["Movie_Title"]
result=df["Movie_Title"].head()
result=df[["Movie_Title","Rating"]].head()
result=df[["Movie_Title","Rating"]].tail(7)
result=df[5:][["Movie_Title","Rating"]].head()
result=df[df["Rating"]>8][["Movie_Title","Rating"]].head(50)
result=df[(df["YR_Released"]>=2014) & (df["YR_Released"]<=2015)]["Movie_Title"]
result=df[(df["Num_Reviews"]>100000) | ((df["Rating"]>=8) & (df["Rating"]<=9))][:]
print(result)
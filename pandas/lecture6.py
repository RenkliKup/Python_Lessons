import numpy as np
import pandas as pd

data=np.random.randint(10,100,75).reshape(15,5)

df=pd.DataFrame(data,columns=["A","B","C","D","E"])
result=df
result=df.columns#kolon bilgileri getiriyor!!!
result=df.head()#ilk 5 satır
result=df.head(10)#ilk 10 satır
result=df.tail()#sondan 5 satır
result=df.tail(10)#sondan 10 satır
result=df["A"].head()#A kolonundaki 5 satır
result=df[["A","B"]].head()#A,B kolonundaki ilk 5 satır
result=df[["A","B"]].tail()#A,B kolonundaki son 5 satır
result=df[5:15][["A","B"]].head()#A,B kolonundaki 5 satır
result=df[5:15][["A","B"]].tail()#A,B kolonundaki son 5 satır
result=df[(df["A"]>50) & (df["A"]<70)][["A","B"]]
result=df[(df["A"]>50) | (df["A"]<70)][["A","B"]]
result=df[(df["A"]>50) | (df["B"]<70)][["A","B"]]
result=df[(df["A"]>50) | (df["B"]>70)][["A","B"]]
result=df[(df["A"]>50) & (df["B"]>70)][["A","B"]]
result=df.query("A>50 & B%2==0")[["A","B"]]
print(result)

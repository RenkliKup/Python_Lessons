import pandas as pd
import numpy as np

data=np.random.randint(10,100,15).reshape(5,3)
df=pd.DataFrame(data,index=["a","c","e","f","h"],columns=["A","B","C"])
df=df.reindex(["a","b","c","d","e","f","g","h"])
result=df.drop(["A","B"],axis=1)
result=df.drop(["b","c"],axis=0)
result=df.isnull()
result=df.notnull()
result=df.isnull().sum()
result=df["A"].isnull().sum()
newColumn=[np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["D"]=newColumn
result=df
result=df[df["A"].isnull()]["A"]
result=df[df["A"].notnull()]["A"]
result=df.dropna(axis=1)#axis=0 nan ları siliyoruz
result=df.dropna()#axis=0 nan ları siliyoruz
result=df.dropna(how="all")#axis=0 nan ları siliyoruz
result=df.dropna(subset=["A","B"],how="any")
result=df.dropna(thresh=2)# en az 2 veya fazla nan olmayan değer varsa silme
result=df.dropna(thresh=4)#en 4 nan olmayan
#result=df.fillna(value=)
result=df.sum().sum()
result=df.size
result=df.isnull().sum().sum()
def ortalama(df):
    toplam=df.sum().sum()
    boyut=df.size- df.isnull().sum().sum()
    return toplam/boyut
result=df.fillna(value=ortalama(df))
print(result)
import pandas as pd
import numpy as np



data={
    "Column1":[1,2,3,4,5],
    "Column2":[10,20,13,20,25],
    "Column3":["abc","bca","ade","cba","dea"]
}
def kare_al(x):
    return x*x
df=pd.DataFrame(data)
result=df
result=df["Column2"].unique()#tekrarlayan elemanlar yok
result=df["Column2"].nunique()#tekrarlanmayan elemanların sayısı
result=df["Column2"].value_counts()#elemanlar kaç kez tekrarlanıyor
result=df["Column2"].apply(kare_al)
df["Column4"]=df["Column3"].apply(len)
result=df.sort_values("Column2")#artan
result=df.sort_values("Column2",ascending=False)#azalan


print(result)
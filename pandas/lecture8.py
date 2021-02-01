import pandas as pd
import numpy as np
from pandas.core import groupby

personeller={"Çalışanlar":["Ahmet Yılmaz","Can Ertürk","Hasan Korkmaz","Cenk Saymaz","Ali Ertürkler"],
    "Departman":["İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları","Junior Dev."],
    "Yaş":[30,25,45,50,24],
    "Semt":["Kadıköy","Tuzla","Maltepe","Tuzla","Maltepe"],
    "Maaş":[500,5000,50,5,1]
    }
    

df=pd.DataFrame(personeller)
result=df[df["Semt"]=="Kadıköy"]["Maaş"].mean()
result=df[df["Semt"]=="Kadıköy"]["Maaş"].sum()
result=df.groupby("Departman").groups
result=df.groupby(["Departman","Semt"]).groups  
semt=df.groupby("Semt")
departman=df.groupby("Departman")
'''
for i,j in semt:
    print(i)
    print(j)
'''
'''
for i,j in departman:
    print(i)
    print(j)
'''
result=df.groupby("Semt").get_group("Tuzla")#Tuzladakileri getir
result=df.groupby("Departman").sum()
result=df.groupby("Departman").mean()
result=df.groupby("Departman")["Maaş"].mean()
result=df.groupby("Semt")["Yaş"].mean()
result=df.groupby("Semt")["Çalışanlar"].count()
result=df.groupby("Departman")["Yaş"].max()
result=df.groupby("Departman")["Yaş"].min()
result=df.groupby("Departman")["Maaş"].min()
result=df.groupby("Departman")["Maaş"].max()["Muhasebe"]
result=df.groupby("Departman").agg(np.mean)
result=df.groupby("Departman")["Maaş"].agg([np.mean,np.max,np.sum,np.min]).loc["Muhasebe"]

print(result)
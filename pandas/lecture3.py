import pandas as pd
import numpy as np
'''
s1=pd.Series([3,2,0,1])
s2=pd.Series([0,3,7,2])
data=dict(apples=s1,oranges=s2)
df=pd.DataFrame(data)'''
#df=pd.DataFrame()
#df=pd.DataFrame([1,2,3,4,5])
#df=pd.DataFrame([["Barış",100],["Beyza",1000]],columns=["Name","Grade"])
dict_list=[
    {"Name":"Barış","Grade":100},
    {"Name":"Mehmet","Grade":80},
    {"Name":"Ümit","Grade":70}
            ]
df=pd.DataFrame(dict_list,index=[1,2,3])
print(df)
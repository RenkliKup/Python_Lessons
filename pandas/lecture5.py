import pandas as pd
import numpy as np
from numpy.random import randn

df=pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["X","Y","Z"])
result=df
result=df["X"]
result=df[["X","Z"]]#kolonları getirir
result=df.loc["A"]#satırları alır
#loc["row","column"]=>loc["row"]=>loc[:,"column"]
result=df.loc[:,"X"]
result=df.loc["B",["X","Y"]]
result=df.loc[:,"X":"Z"]
result=df.loc[:,:"Z"]
result=df.loc["A":"C",:"Z"]
result=df.loc[:"C",:"Z"]
df["W"]=pd.Series(randn(3),["A","B","C"])
df["T"]=df["X"]+df["Y"]
df.drop(["T","X"],axis=1,inplace=True)#yukarıdan aşağıya silme
print(df)
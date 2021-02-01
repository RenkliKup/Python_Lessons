import pandas as pd
import numpy as np

'''
pandas_series=pd.Series()
print(pandas_series)
'''
'''
num=[1,2,3,4,5]
pandas_series=pd.Series(num)
print(pandas_series)
'''
'''
letter=["1","2","3","4","5"]
pandas_series=pd.Series(letter)
print(pandas_series)
'''
'''
scalar=5
pandas_series=pd.Series(scalar,['a','b','c','d','e'])
print(pandas_series)
'''

num=[1,2,3,4,5]
pandas_series=pd.Series([1,2,3,4,5],["a","b","c","d","e"])
print(pandas_series)

'''
dic={'a':10,'b':20,'c':30}
pandas_series=pd.Series(dic)
print(pandas_series)
'''
'''
random_numbers=np.random.randint(10,100,6)
pandas_series=pd.Series(random_numbers)
print(pandas_series)
'''
result=pandas_series['a':'d':2]
result=pandas_series[-1]
result=pandas_series[:2]
result=pandas_series[-2:]
result=pandas_series.ndim#kaç boyutlu?
result=pandas_series.dtype
result=pandas_series.shape
result=pandas_series.sum()
result=pandas_series.max()
result=pandas_series.min()
result=pandas_series+pandas_series
result=pandas_series+50
result=np.sqrt(pandas_series)
result=pandas_series >=3
result=pandas_series %2==0
#print(pandas_series[result])çift sayılar
#print(result)
opel2018=pd.Series([10,20,30,40,50],["astra","corsa","mokka","insignia"])
opel2019=pd.Series([10,20,30,40,50],["astra","corsa","Grandland","insignia"])
total=opel2018+opel2019
print(total["corsa"])


import numpy as np

#numpy dizi methodları

result=np.random.randint(0,30,[5,5])
result=np.arange(30).reshape(5,6)
result=np.arange(30).reshape(5,6).max()
result=np.random.randint(1,100,[4,4]).max()
result=np.random.randint(1,100,[4,4]).min()
result=np.random.randint(1,100,[4,4]).argmax()#en yüksek kaçıncı indexte olduğunu döndürür
result=np.random.randint(1,100,[4,4]).argmin()#en düşük kaçıncı indexte olduğunu döndürür
result=np.random.randint(0,30,[5,5]).shape
print(result)
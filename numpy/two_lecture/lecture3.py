import numpy as np

#random

result=np.random.randn(4)
result=np.random.randn(4,4)
#randint(start,stop,how much)
result=np.random.randint(1,20)
result=np.random.randint(1,10,25)
result=np.random.randint(1,300,25).reshape(5,5)
print(result)
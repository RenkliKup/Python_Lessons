import numpy as np

#matrix
ornekmatris=np.random.randint(100,500,[3,3])
#print(ornekmatris[0][0])
#print(ornekmatris[0,2])
#print(ornekmatris[:,2])
result=np.random.randint(0,30,[5,5])
yenidizi=result[[0,2,4]]
print(yenidizi)
print(result)


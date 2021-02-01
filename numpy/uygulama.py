import numpy as np

numpy_array=np.array([10,15,30,45,60])
numpy_array=np.arange(5,16)
numpy_array=np.arange(50,105,step=5)
numpy_array=np.zeros(10)
numpy_array=np.ones(10)
numpy_array=np.linspace(0,100,5)
numpy_array=np.random.randint(10,30,5)
numpy_array=np.random.randn(10)
numpy_array=np.random.randint(10,50,15).reshape(3,5)
numpy_array_row=numpy_array.sum(axis=1)#sutun row axis=1 satır column axis=0
numpy_array_col=numpy_array.sum(axis=0)
#print(numpy_array_row)
#print(numpy_array_col)
max1=numpy_array.max()
min1=numpy_array.min()
print(max1," ,",min1)
print(numpy_array)

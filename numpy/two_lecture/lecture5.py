import numpy as np

benimdizim=np.arange(0,15)
benimdizim[3:8]=-5
baskadizi=np.arange(0,24)
result=baskadizi[4:9]
result[:]=700#kopyalanan dizi adresi aynı olur
result=baskadizi
ornekdizi=np.arange(0,24)
ornekdizikopyasi=ornekdizi.copy()#kopyalanan dizi adresi farklı olur
ornekdizikopyasi[:]=700
print(ornekdizi)
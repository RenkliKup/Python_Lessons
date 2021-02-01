import numpy as np

#operasyonlar

yeniBirDizi=np.random.randint(1,100,20)
x=yeniBirDizi>36
y=yeniBirDizi[x]
z=yeniBirDizi[yeniBirDizi>66]
sondizi=np.arange(0,24)
p=sondizi+sondizi
p=sondizi-sondizi
p=sondizi*sondizi
p=sondizi/sondizi
p=np.sqrt(sondizi)
p=np.max(sondizi)
p=np.min(sondizi)
print(p)

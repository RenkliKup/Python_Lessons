
import matplotlib.pyplot as plt
import numpy as np
'''
x=[1,2,3,4]
y=[1,4,9,16]
plt.plot(x,y,color="red",linewidth=2,linestyle="--",marker="o")
plt.axis([0,6,0,20])#0 6 x değerlerinin max ve min degeri 0 20 y degerlerinin max ve min i
plt.title("Grafik Başlığı")
plt.xlabel("x label")
plt.ylabel("y label")
'''

x=np.linspace(0,2,100)
'''
plt.plot(x,x,label="linear",linestyle="--")
plt.plot(x,x**2,label="quadratic",linestyle="dashed")
plt.plot(x,x**3,label="cubic",linestyle="dotted")
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("simple plot")
plt.grid()

plt.legend()
plt.show()
'''
fig,axs=plt.subplots(2)
axs[0].plot(x,x,color="red",label="Linear")
axs[1].plot(x,x**2,color="green",Label="quadradic")
plt.legend()
plt.show()
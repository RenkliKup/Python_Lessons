import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-10,9,20)
y=x**3
z=x**2
'''
fig=plt.figure()

axes=fig.add_axes([0.15,0.15,0.8,0.8])
axes.plot(x,y,"--",label="quadratic")
axes.set_xlabel("x label")
axes.set_ylabel("y label")
axes.set_title("Cubic")
axes.legend()

axes2=fig.add_axes([0.5,0.7,0.3,0.2])
axes2.plot(x,y,"--",label="quadratic")
axes2.set_xlabel("x label")
axes2.set_ylabel("y label")
axes2.set_title("Cubic")
axes2.legend()
plt.show()
'''
fig=plt.figure()
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,z,"--",label="square")
axes.plot(x,y,"o",label="cubic")
axes.legend()
plt.show()
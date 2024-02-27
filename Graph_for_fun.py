import math
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi,100)
y1=x**2
y2=x**2+2*x+1
y3=np.sin(x)-np.tan(x)-7*x**3
y4=16*x**2-9
y5=17-69*x**(1/2)
y6=700*np.sin(x)*np.cos(x)
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.plot(x,y5)
plt.plot(x,y6)
plt.show()
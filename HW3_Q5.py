import numpy as np
import matplotlib.pyplot as plt
import math
x=np.linspace(-2*math.pi,2*math.pi,200)
y=x-4*np.sin(2*x)-3
x2=np.linspace(-2*math.pi,2*math.pi,200)
y2=x*0
plt.plot(x,y)
plt.plot(x2,y2)
plt.show()
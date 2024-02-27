import numpy as np
import math
import matplotlib.pyplot as plt
theta = np.linspace(0,2*np.pi,100)
R = 1.2
sigma_r = 0.1
f = 15
p = 0
x = R*(1+sigma_r*(f*theta+p))*np.cos(theta)
y = R*(1+sigma_r*(f*theta+p))*np.sin(theta)
plt.plot(x,y)
plt.show()
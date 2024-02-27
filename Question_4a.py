import numpy as np
import matplotlib.pyplot as plt
import math
t=np.linspace(0,math.pi,31)
y=np.cos(t)
sum = sum(t*y)
print ("The sum is " +str(sum))
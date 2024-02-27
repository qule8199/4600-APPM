import math
import numpy as np
h=0.01/(2**(np.arange(0,10)))
#function=cos(X)
x=math.pi/2
print([(np.cos(x+n)-np.cos(x))/n for n in h])   

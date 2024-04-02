import numpy as np
import math
from scipy import io, integrate, linalg, signal
from scipy.integrate import quad
import matplotlib.pyplot as plt
def driver():
    x=2
    n=2
    phi_0=1
    phi_1=x
    vector=[]
    for l in range(1,n+1):
        vector.append(eval_legendre(l,x))
        print(vector)
x=2
values=[1,x]
def eval_legendre(n,x):
    eval = 1/(n+1)*((2*n+1)*x*values[n]-n*values[n-1])
    values.append(eval)
    return eval

driver()
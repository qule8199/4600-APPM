import numpy as np
def driver():
#function
     f1 = lambda x: x-4*np.sin(2*x)-3

     Nmax=1000
     tol=1e-10
# test the function
     x0 = 0
     [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)

def fixedpt(f,x0,tol,Nmax):
    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''
    count = 0
    '''NEW'''
    vector_guesses = [x0]
    while (count<Nmax):
        x1=f(x0)
        vector_guesses.append(x1)
        count=count+1
        if (abs(x1-x0)<tol):
            xstar = x1
            ier = 0
            print("The approximations are: ", vector_guesses)
            print("Number of approximations: ",len(vector_guesses))
            return [xstar,ier]
        x0=x1
    xstar = x1
    ier=1
    print("The guesses were: ",vector_guesses)
    return [xstar,ier]

driver()
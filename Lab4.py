import numpy as np
def driver():
#function
     f1 = lambda x: (10/(x+4))**0.5

     Nmax=100
     tol=1e-10
# test the function
     x0 = 1.5
     [xstar,ier], vector_guesses = fixedpt(f1,x0,tol,Nmax)
     new_vector = aitkins(vector_guesses)
     print('the approximate fixed point is:',xstar)
     print(new_vector)
     #print('f1(xstar):',f1(xstar))
     #print('Error message reads:',ier)

    
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
            return [xstar,ier], vector_guesses
        x0=x1
    xstar = x1
    ier=1
    #print("The guesses were: ",vector_guesses)
    return [xstar,ier]

def aitkins(a):
    new_vec=[]
    vector_guesses=a
    for n in range(len(vector_guesses)-2):
        pn=a[n]-((a[n+1]-a[n])**2)/(a[n+2]-2*a[n+1]+a[n])
        new_vec.append(pn)
    print(f"The new vector has {len(new_vec)} iterations")
    return new_vec
driver()
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import scipy.linalg as scila
import time

def driver():

     ''' create  matrix for testing different ways of solving a square 
     linear system'''

     '''' N = size of system'''
     N = 5000
 
     ''' Right hand side'''
     b = np.random.rand(N,1)
     A = np.random.rand(N,N)
     '''Time check 1'''
     t_0 = time.perf_counter_ns()
     '''Constructing Factorization'''
     lu,piv=scila.lu_factor(A)
     '''Time check 2'''
     t_1 = time.perf_counter_ns()
     '''Solving LU Factorization'''
     x_lu = scila.lu_solve((lu,piv),b)
     '''Time check 3'''
     t_2 = time.perf_counter_ns()


     test_lu = np.matmul(A,x_lu)
     r_lu = la.norm(test_lu-b)
     print(r_lu)
     print("Factoring takes "+str((t_1-t_0)/1000000000)+" seconds")
     print("Solving takes "+str((t_2-t_1)/1000000000)+" seconds")
     '''Non-LU factorization solve'''
     '''Time Check non-Lu'''
     t0 = time.perf_counter_ns()
     x = scila.solve(A,b)
     '''Time check'''
     t1 = time.perf_counter_ns()
     test = np.matmul(A,x)
     r = la.norm(test-b)
     print(r)
     print("solving non-lu takes "+str((t1-t0)/1000000000)+" seconds")

     ''' Create an ill-conditioned rectangular matrix '''
     N = 10
     M = 5
     A = create_rect(N,M)     
     b = np.random.rand(N,1)


     
def create_rect(N,M):
     ''' this subroutine creates an ill-conditioned rectangular matrix'''
     a = np.linspace(1,10,M)
     d = 10**(-a)
     
     D2 = np.zeros((N,M))
     for j in range(0,M):
        D2[j,j] = d[j]
     
     '''' create matrices needed to manufacture the low rank matrix'''
     A = np.random.rand(N,N)
     Q1, R = la.qr(A)
     test = np.matmul(Q1,R)
     A =    np.random.rand(M,M)
     Q2,R = la.qr(A)
     test = np.matmul(Q2,R)
     
     B = np.matmul(Q1,D2)
     B = np.matmul(B,Q2)
     return B     
          
  
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()       

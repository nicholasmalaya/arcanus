#!/bin/py
#
# inexact Newton-conjugate gradient method
#
# solve: 
#        min f(x) = 1/2 x.t (I + mu * A) x + sigma/4 (x.t A x)^2
#
import numpy as np

def mycg(A,b,maxiter,tol,x):
    """ Conjugate Gradient Method. """
    """ MYCG(A,B,maxiter,tol,x0) solves the system of linear equations A*X=B """
    """ for X. The N-by-N coefficient matrix A must be symmetric and the right"""
    """hand side column vector B must have length N."""
    
    r = A * np.transpose(x) - b
    d = -r
    print d
    rsold = np.transpose(r)*r

    for i in xrange(1,maxiter):
        Ad = np.dot(A,d)
        alpha = rsold/np.dot(d,Ad)
        x = x+alpha*np.transpose(d)
        r = np.dot(r,alpha*Ad)
        rsnew = np.transpose(r)*r
        if np.sqrt(rsnew)<tol:
            break
        
        beta = rsnew/rsold
        d = beta*np.transpose(d)-r
        rsold = rsnew
    return d


# parameters
sigma = 1.0
mu    = 10.0

#A = np.matrix('5 1 0 0.5; 1 4 0.5 0; 0 0.5 3 0; 0.5  0 0 2')
A = np.matrix('4 -1 1; -1 4 -2; 1 -2 4')
b = np.array([12, -1, 5])
x = np.transpose(np.array([1, -1,  2]))

#x  = np.array([np.cos(70),np.sin(70),np.cos(70),np.sin(70)])

# identity matrix
I = np.identity(len(A))

if __name__ == '__main__':
    """Main function"""
    print A       
    print I
    print b
    print mycg(A,b,1000,.0001,x)

#
# nick 
# 2/25/14
#

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
    
    r = A*x-b;
    d = -r;
    #rsold = r'*r;

    for i=1:maxiter:
        Ad = A*d;
        #alpha = rsold/(d'*Ad);
        x = x+alpha*d;
        r = r+alpha*Ad;
        #rsnew = r'*r;
        if sqrt(rsnew)<tol:
            break

        beta = rsnew/rsold;
        d = -r+beta*d;
        rsold = rsnew;
    end



# parameters
sigma = 1.0
mu    = 10.0

A = np.matrix('5 1 0 0.5; 1 4 0.5 0; 0 0.5 3 0; 0.5  0 0 2')

# identity matrix
I = np.identity(len(A))

if __name__ == '__main__':
    """Main function"""
    print A       
    print I

#
# nick 
# 2/25/14
#

#!/bin/py
#
# inexact Newton-conjugate gradient method
#
# solve: 
#        min f(x) = 1/2 x.t (I + mu * A) x + sigma/4 (x.t A x)^2
#
import numpy as np

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

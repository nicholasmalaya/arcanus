#
#
#

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab


def hpd(pdf, obs):
    """ Returns beta"""
    beta = 0.0


    return beta


#
# main function
# 
if __name__ == '__main__':
    mean = 0
    variance = 1
    sigma = np.sqrt(variance)
    x     = np.linspace(-3,3,100)
    pdf   = mlab.normpdf(x,mean,sigma)
    plt.plot(x,pdf)    
    plt.show()

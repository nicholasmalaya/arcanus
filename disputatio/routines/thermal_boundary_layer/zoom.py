#!/bin/py
#
#
# power law scaling thermal layer
#
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#
# read in data
#
def read_dat():
    x = []
    t = []

    f = open('data.dat', 'r')
    for line in f:
        values = line.split("\t")
        values = line.split("\t")
        x.append(float(values[0]))
        print values[1].split("\n")[0]
        t.append(float(values[1].split("\n")[0]))
    f.close()
    
    return x,t

def e(x):
    c = 150.0
    exxp = 42+20*np.exp(-np.array(x)*c)
    return exxp

#
#
#
def plot_raw(x,t):
    mx = 5
    order = 4
    print x[0:mx],t[0:mx]
    pp = np.poly1d(np.polyfit(x[0:mx],t[0:mx],order))
    xx = np.arange(0,x[mx],.01)

    #log_lst = np.log(lst)
    #print log_lst
    plt.subplot(1, 1, 1)
    plt.plot(x,t, 'ko-',color='blue',label='Raw')
    plt.title('Thermal Boundary Layer Measured')
    plt.xlabel('Location Above Ground (Meters)')
    plt.ylabel('Temperature (Celsius)')
    plt.legend()

    full=1

    if(full):
        plt.xlim((0,.35))
        plt.ylim((40,65))
    else:
        plt.xlim((0,2.35))
        plt.ylim((35,65))
        
    # plot exponential
    plt.plot(xx,e(xx), 'ko-',color='red',label='exponential')

    # plot polynomial:
    #plt.plot(xx,pp(xx), 'ko-',color='red',label='fit')

    #
    ## execute!
    #
    plt.show()

    print 'Peak velocity modelled is: ',e(0)

def main():
    # my code here
    x,t = read_dat()
    plot_raw(x,t)

# execute
if __name__ == "__main__":
    main()

#
# nick 
# 8/5/16
#

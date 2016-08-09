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
        #print values[1].split("\n")[0]
        t.append(float(values[1].split("\n")[0]))
    f.close()
    
    return x,t

def e(x, a, b, c):
    return a * np.exp(-b * x) + c

#def e(x):
#    c = 240.0
#    exxp = 42+30*np.exp(-np.array(x)*c)
#    return exxp

#
#
#
def plot_raw(x,t):
    mx = 4
    order = 4
    print x[0:mx]
    print t[0:mx]
    #pp = np.poly1d(np.polyfit(x[0:mx],t[0:mx],order))
    xx = np.arange(0,x[mx],.001)

    #
    # find ideal exp coefficients
    #
    from scipy.optimize import curve_fit
    popt, pcov = curve_fit(e, x[0:mx], t[0:mx])

    print popt

    #log_lst = np.log(lst)
    #print log_lst
    plt.subplot(1, 1, 1)
    plt.plot(x,t, 'ko',color='blue',label='Raw',markersize=10)
    plt.title('Thermal Boundary Layer Measured')
    plt.xlabel('Location Above Ground (Meters)')
    plt.ylabel('Temperature (Celsius)')
    plt.legend()

    plt.xlim((-.05,.35))
    plt.ylim((40,75))
        
    #
    # http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
    # and,
    # http://stackoverflow.com/questions/3433486/how-to-do-exponential-and-logarithmic-curve-fitting-in-python-i-found-only-poly
    #
    # plot exponential
    plt.plot(xx,e(xx,popt[0],popt[1],popt[2]), 'ko-', color='red',label='exponential')

    # plot polynomial:
    #plt.plot(xx,pp(xx), 'ko-',color='red',label='fit')

    #
    ## execute!
    #
    #plt.show()
    plt.savefig('fit_zoomed.png')

    # unzoom
    plt.xlim((0,2.35))
    plt.savefig('fit.png')

    print 'Peak temp is: ',e(0,popt[0],popt[1],popt[2])
    print 'Gradient is: ', e(0,popt[0],popt[1],popt[2])-t[-1]

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

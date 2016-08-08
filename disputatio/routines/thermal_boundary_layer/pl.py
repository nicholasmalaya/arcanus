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

#
#
#
def plot_raw(x,t):
    #log_lst = np.log(lst)
    #print log_lst
    plt.subplot(1, 1, 1)
    plt.plot(x,t, 'ko-',color='blue',label='Raw')
    plt.title('Thermal Boundary Layer Measured')
    plt.xlabel('Location Above Ground (Meters)')
    plt.ylabel('Temperature (Celsius)')
    plt.legend()
    plt.show()

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

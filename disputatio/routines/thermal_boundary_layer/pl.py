#!/bin/py
#
#
# power law scaling of companies
#
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#
# read in data
#
def read_dat():
    lst = []

    f = open('data.dat', 'r')
    for line in f:
        values = line.split("\t")
        lst.append(float(values[3]))        
    f.close()
    
    return lst

#
#
#
def plot_raw(lst):
    log_lst = np.log(lst)
    print log_lst
    plt.subplot(1, 1, 1)
    plt.plot(lst, 'ko-',color='blue',label='Raw')
    plt.title('Market Capitalization of Largest Companies')
    plt.ylabel('$')
    plt.legend()
    plt.show()

def main():
    # my code here
    mrk_cap = read_dat()
    plot_raw(mrk_cap)

# execute
if __name__ == "__main__":
    main()

#
# nick 
# 8/5/16
#

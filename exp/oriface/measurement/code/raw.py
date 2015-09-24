#!/bin/py
#
# open file
# read contents
# (re)start when third column found
#
import sys
import numpy as np

def autocorr(x):
    result = np.correlate(x, x, mode = 'full')
    maxcorr = np.argmax(result)
    #print 'maximum = ', result[maxcorr]
    result = result / result[maxcorr]     # <=== normalization

    return result[result.size/2:]

def plot_series(time,voltage,name):
    v  = [float(i) for i in voltage]
    t  = [float(i) for i in time]
    print name
    avg  = np.mean(v)
    sig  = np.std(v)
    up   = avg+2*sig
    down = avg-2*sig
    print 'mean: ', avg
    print 'std : ', sig

    import matplotlib.pyplot as plt

    #
    # first, time series data
    #
    plt.subplot(1, 1, 1)
    plt.title('Oriface Meter Raw Time Series Data')
    plt.plot(t,v,  'ko-',color='blue') #label=name,
    plt.ylabel('Voltage')
    plt.xlabel('Time (Seconds)')

    plt.axhline(y=avg, xmin=0, xmax=1, hold=None,linewidth=4.0,color='black',label='Mean')
    plt.axhline(y=up, xmin=0, xmax=1, hold=None,linewidth=4.0,color='red',label=r'$2\sigma$')
    plt.axhline(y=down, xmin=0, xmax=1, hold=None,linewidth=4.0,color='red')

    #plt.axis([0,1,5.80,5.90])

    plt.legend(loc='best')
    plt.savefig('oriface_time.png')
    plt.close()

    #
    # now, make a histogram!
    # 
    bin_number=25
    pdf,bins,patches = plt.hist(v,bin_number,normed=0)
    plt.ylabel('Frequency')
    plt.xlabel('Voltage')
    plt.savefig('oriface_hist.png')
    plt.close()

    #
    # now make an autocorrelation plot
    #
    #plt.acorr(v,usevlines=True, normed=True, lw=2,maxlags=999)
    a = autocorr(v)
    plt.plot(time,a)
    plt.ylabel('Correlation')
    plt.xlabel('Time')
    plt.savefig('incl_auto.png')

    #
    # steady as she goes!
    #
    return 0

#
# open and read file
#
path="../data/sample_rate_check.lvm"
file = open(path, "r+")

#
# data objects
#
set_names= []
stop=0
time    = []
voltage = []

for line in file:
    #
    # sep by whitespace
    #
    line_list = line.split()

    if( len(line_list) > 2):
        #
        # reset! save name of this set
        #
        if stop < 2:
            stop=stop+1
        else:
            plot_series(time,voltage,set_names[0])
            print 'done with set'
            sys.exit(0)

        set_name=line_list[2:]
        set_names.append(' '.join(set_name))
        time    = [line_list[0]]
        voltage = [line_list[1]]

    else:
        time.append(line_list[0])
        voltage.append(line_list[1])

#
# clean up
#
plot_series(time,voltage,'oriface')
file.close()       

#
# steady as she goes
#
sys.exit(0)

#
# nick 
# 9/23/15
#

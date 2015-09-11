#!/bin/py
#
# open file
# read contents
# (re)start when third column found
#
import sys


#
# open and read file
#
path="../data/statistics_incl.lvm"
file = open(path, "r+")

#
# data objects
#
set_names = []
voltage   = []
std       = []
height    = []

voltage2  = []
std2      = []
height2   = []

for line in file:
    #
    # sep by whitespace
    #
    line_list = line.split()
    set_name=line_list[5:]
    set_names.append(' '.join(set_name))

    if( len(set_names) > 9):
        height2.append(line_list[8])
        voltage2.append(line_list[2])
        std2.append(line_list[3])

    else:
        height.append(line_list[8])
        voltage.append(line_list[2])
        std.append(line_list[3])
#
# clean up
#
file.close()       

#
# least squares curve fit
#
import numpy as np
from scipy import stats
height  = [float(i) for i in height]
voltage = [float(i) for i in voltage]
std     = [float(i) for i in std]

(slope, intercept, r_value, p_value, std_err) = stats.linregress(height,voltage)
print "r-squared:", r_value**2
print  'p_value', p_value
print 'slope: ', slope
print 'std error: ', std_err
print '\sigma x^2: ',sum(height)
#
# calculate uncertainty
#
h = np.array(height)
s = np.array(std)
print len(s)
buff = h*h
uq = 100*2*s*np.sqrt(std_err)*(1.0/len(s) + buff/sum(height))
print uq
#
# plot it!
#
import matplotlib.pyplot as plt
plt.subplot(1, 1, 1)

line = slope*np.array(height) + intercept
plt.errorbar(height, line,color='blue',yerr=uq,label='Least Squares Fit w/ Uncertainty') 
plt.title('Calibration of an Pressure Transducer: Micromanometer')
plt.ylabel('Voltage')
plt.xlabel('Height (Inches)')
plt.legend(loc='best')
plt.savefig('incl-error.png')
plt.close()
#
# steady as she goes
#
sys.exit(0)


#
# nick 
# 9/9/15
#
# old header:
#
# X_Dimension     Time    Time    Time    Time
# X0      0.0000000000000000E+0   0.0000000000000000E+0   0.0000000000000000E+0   0.0000000000000000E+0
# Delta_X 0.001000        0.001000        0.001000        0.001000
# ***End_of_Header***
# X_Value Pressure Transducer Voltage (Arith. Mean)       Pressure Transducer Voltage (Std Dev)   Pressure Transducer Voltage (Variance)  Pressure Transduce\
# r Voltage (Total Samples)     Comment

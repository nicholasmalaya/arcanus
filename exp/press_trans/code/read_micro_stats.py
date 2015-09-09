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
path="../data/statistics_micro2.lvm"
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
        height2.append(line_list[7])
        voltage2.append(line_list[2])
        std2.append(line_list[3])

    else:
        height.append(line_list[7])
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
(slope, intercept, r_value, p_value, std_err) = stats.linregress(height,voltage)
print "r-squared:", r_value**2
print  'p_value', p_value
#
# plot it!
#
import matplotlib.pyplot as plt
plt.subplot(2, 1, 1)
plt.plot(height, voltage,  'ko',label='First Calibration Set',color='blue')
plt.plot(height2, voltage2,'ko',label='Second Calibration Set',color='black')

line = slope*np.array(height) + intercept
print line
plt.plot(height, line, '--k',label='Least Squares Fit') 
plt.title('Calibration of an Pressure Transducer: Micromanometer')
plt.ylabel('Voltage')
plt.xlabel('Height (Inches)')
plt.legend(loc='best')
plt.savefig('micro.png')
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

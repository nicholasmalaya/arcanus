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
        print line_list
#
# clean up
#
file.close()       

#
# plot it!
#
import matplotlib.pyplot as plt
plt.subplot(2, 1, 1)
plt.plot(height, voltage,  'ko',label='First Calibration Set',color='blue')
plt.plot(height2, voltage2,'ko',label='Second Calibration Set',color='black')
plt.title('Calibration of an Pressure Transducer: Inclined Manometer')
plt.ylabel('Voltage')
plt.xlabel('Height (Inches)')
plt.legend(loc='best')
plt.show()
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

#!/bin/py
#
# open file
# read contents
# (re)start when third column found
#
import sys
import numpy as np

#
# open and read file
#
path = "def2.txt"
file = open(path, "r+")
defect1 = []
for line in file:
    defect1.append(float(line))

path = "def10.txt"
file = open(path, "r+")
defect2 = []
for line in file:
    defect2.append(float(line))

path = "yd2.txt"
file = open(path, "r+")
yd1 = []
for line in file:
    yd1.append(float(line))
    
path = "yd10.txt"
file = open(path, "r+")
yd2 = []
for line in file:
    yd2.append(float(line))
    
#
# plot
#
import matplotlib.pyplot as plt
plt.subplot(1, 1, 1)
plt.plot(yd1,defect1,color='black',marker='o',label=r'$y/d=5$')
plt.plot(yd2,defect2,color='blue', marker='v',label=r'$y/d=10$')
plt.title('LDV Streamwise Velocity 5v10')
plt.ylabel(r'$U/U_{\infty}$')
plt.xlabel('y/d')
plt.legend(loc='best')
plt.savefig('defect10.png')
plt.close()

#
# steady as she goes
#
sys.exit(0)

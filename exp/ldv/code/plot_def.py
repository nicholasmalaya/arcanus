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
path = "def1.txt"
file = open(path, "r+")
defect1 = []
for line in file:
    defect1.append(float(line))

path = "def2.txt"
file = open(path, "r+")
defect2 = []
for line in file:
    defect2.append(float(line))

path = "yd1.txt"
file = open(path, "r+")
yd1 = []
for line in file:
    yd1.append(float(line))
    
path = "yd2.txt"
file = open(path, "r+")
yd2 = []
for line in file:
    yd2.append(float(line))
    
#
# plot
#
import matplotlib.pyplot as plt
plt.subplot(1, 1, 1)
plt.plot(yd1,defect1,color='black',marker='o',label='First Set')
plt.plot(yd2,defect2,color='blue',marker='v',label='Second Set')
plt.title('LDV Defect 5d')
plt.ylabel(r'$U/U_{\infty}$')
plt.xlabel('y/d')
plt.legend(loc='best')
plt.savefig('defect.png')
plt.close()

#
# steady as she goes
#
sys.exit(0)

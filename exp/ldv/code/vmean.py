#!/bin/py
#
# open file
# read contents
# (re)start when third column found
#
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt

#
# open and read file
#
path = "vmean_5.txt"
file = open(path, "r+")
defect1 = []
for line in file:
    defect1.append(float(line))

path = "vmean_10.txt"
file = open(path, "r+")
defect2 = []
for line in file:
    defect2.append(float(line))

path = "vmean_yd.txt"
file = open(path, "r+")
yd = []
for line in file:
    yd.append(float(line))

path = "vmean_yd10.txt"
file = open(path, "r+")
yd2 = []
for line in file:
    yd2.append(float(line))

print len(defect1)
print len(defect2)
print len(yd)
#
# plot
#
plt.subplot(1, 1, 1)
plt.plot(yd,defect1,color='blue',marker='o',label=r'$y/d=5$')
plt.plot(yd2,defect2,color='black', marker='v',label=r'$y/d=10$')
plt.title('LDV VMEAN')
plt.ylabel(r'$V_{mean}/U_{\infty}$')
plt.xlabel('y/d')
plt.legend(loc='best')
plt.savefig('vmean.png')
plt.close()

#
# steady as she goes
#
sys.exit(0)

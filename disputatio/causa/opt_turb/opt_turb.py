#!/bin/py
#
# determine optimal energy from flow
#
#
#
# Radius VT  Vz
# m      m/s m/s
#
#
import numpy as np
import matplotlib.pyplot as plt

#
# first, import the data from drag.dat
#
drag_fl = 'drag.dat'
ar_sz = sum(1 for line in open(drag_fl))
r  = np.empty(ar_sz)
vt = np.empty(ar_sz)
vz = np.empty(ar_sz)

f = open(drag_fl, 'r+')
it=0
for line in f:
    rr,vvt,vvz = line.split()
    r[it]  =rr
    vt[it] =vvt
    vz[it] =vvz
    it=it+1
f.close()

#
# now, 
#
print vt
#
# nick
# 6/07/2016
#

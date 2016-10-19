# "T","u","v","w","p","k","mu",
# "vel_penalty_:0","vel_penalty_:1","vel_penalty_:2",
# "vel_source_:0","vel_source_:1","vel_source_:2",
# "Points:0","Points:1","Points:2"


# "T","u","v","w","p","k","mu","vel_penalty_:0","vel_penalty_:1","vel_penalty_:2","vel_source_:0","vel_source_:1","ve#l_source_:2","Points:0","Points:1","Points:2"
#
#
# read CSV and import into plot
# 14,15,16

import csv

ifile  = open('vertical.csv', "rb")

# stupid initialization of list
T = []
u = []
v = []
w = []
height = []

csvReader1 = csv.reader(ifile)
for row in csvReader1:
    x      = row[13]
    y      = row[14]
    height.append(row[15])

ifile.close()

import numpy as np
#
#
#


#
# plot
#
import matplotlib.pyplot as plt

# plt.plot(x, y)

plt.plot(height,'--', label='Simulation',linewidth=3)

#plt.ylim([0,3])
#plt.xlim([0,5])


#
#
fsz=20
plt.ylabel(r'$u_{\theta}/u^{Max}_{\theta}$',fontsize=fsz,rotation="0",labelpad=20)
plt.xlabel(r'$r/r^{Max}$',fontsize=fsz)
plt.legend(loc='best')
plt.axes().set_aspect('equal', 'datalim')



#plt.show()
plt.tight_layout()
plt.savefig('bl.png')

#
#
#

#
# nick
#

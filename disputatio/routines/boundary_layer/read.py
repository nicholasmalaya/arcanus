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

ifile  = open('vertical0.csv', "rb")

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

height = np.array(height)
print height.sort()

l = np.arange(len(height))
fit = (np.exp(.06*l) -1.0)/20.

#
# plot
#
import matplotlib.pyplot as plt

# plt.plot(x, y)

plt.plot(height,'x--', label='Simulation',linewidth=3)
plt.plot(fit,'x--', label='Fit',linewidth=3)

#plt.ylim([0,3])
#plt.xlim([0,5])


#
#
fsz=20
plt.ylabel(r"$z'$",fontsize=fsz,rotation="0",labelpad=20)
plt.xlabel(r'$index$',fontsize=fsz)
plt.legend(loc='best')
#plt.axes().set_aspect('equal', 'datalim')



#plt.show()
plt.tight_layout()
plt.savefig('bl.png')

#
#
#

#
# nick
#

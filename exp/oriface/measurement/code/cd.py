#!/bin/py
#
# open file
# read contents
# (re)start when third column found
#
import sys

def read_set(path):
    
    #
    # data
    # 
    set_names = []
    orm       = []
    lfe       = []

    file = open(path, "r+")
    for line in file:
        #
        # sep by whitespace
        #
        line_list = line.split()
        set_name=line_list[3:]
        set_names.append(' '.join(set_name))

        orm.append(line_list[1])
        lfe.append(line_list[2])

    #
    # clean up
    #
    file.close()       

    #
    # exit
    #
    return set_names,orm,lfe

if __name__ == "__main__":
    import numpy as np

    # -------------------------------------------------------------------------------
    # open and read file
    # -------------------------------------------------------------------------------
    path1="../data/series1.lvm"
    path2="../data/series2.lvm"

    s1,o1,l1 = read_set(path1)
    s2,o2,l2 = read_set(path2)    

    # -------------------------------------------------------------------------------
    # Calculate Qs
    # -------------------------------------------------------------------------------
    rho = 0.074887
    mu  = 3.8364971e-7
    nu  = mu/rho
    d   = 1.8227
    D   = 4.0
    beta = d/D

    l1 = np.array(map(float, l1))
    l2 = np.array(map(float, l2))

    q1 = 20.5*1.004*l1
    q2 = 20.5*1.004*l2

    re1 = q1 * D /(np.pi*nu*(d**2.0)/4.0)
    re2 = q2 * D /(np.pi*nu*(d**2.0)/4.0)

    cd1 = q1 * ((1-beta**4)**(0.5) /(np.pi*(d**2.0)/4.0)) * (rho/(2*l1))**0.5
    cd2 = q2 * ((1-beta**4)**(0.5) /(np.pi*(d**2.0)/4.0)) * (rho/(2*l2))**0.5

    # -------------------------------------------------------------------------------
    # least squares curve fit
    # -------------------------------------------------------------------------------

    # import numpy as np
    # from scipy import stats
    # height  = [float(i) for i in height]
    # voltage = [float(i) for i in voltage]
    # (slope, intercept, r_value, p_value, std_err) = stats.linregress(height,voltage)
    # print "r-squared:", r_value**2
    # print  'p_value', p_value
    # print 'slope: ', slope

    # -------------------------------------------------------------------------------
    # plot it!
    # -------------------------------------------------------------------------------
    import matplotlib.pyplot as plt
    plt.subplot(1, 1, 1)
    plt.plot(re1, cd1, 'ko',label='First Calibration Set',color='blue')
    plt.plot(re2, cd2, 'ko',label='Second Calibration Set',color='black')

    #line = slope*np.array(height) + intercept
    #print line
    #plt.plot(height, line, '--k',label='Least Squares Fit') 

    plt.title('Calibration of an Oriface Meter')
    plt.ylabel(r'$C_d$')
    plt.xlabel('Re')
    plt.legend(loc='best')
    plt.savefig('cd.png')
    plt.close()

    #
    # steady as she goes
    #
    sys.exit(0)

# -------------------------------------------------------------------------------
# nick 
# 9/29/15
# -------------------------------------------------------------------------------
# LabVIEW Measurement	
# Writer_Version	2
# Reader_Version	2
# Separator	Tab
# Decimal_Separator	.
# Multi_Headings	No
# X_Columns	One
# Time_Pref	Relative
# Operator	Methods Students
# Description	Don't delete initial header
# Date	2015/09/23
# Time	15:07:04.9949688911437988282
# ***End_of_Header***	
	
# Channels	2		
# Samples	1	1	
# Date	2015/09/23	2015/09/23	
# Time	15:07:04.9949688911437988282	15:07:04.9949688911437988282	
# X_Dimension	Time	Time	
# X0	0.0000000000000000E+0	0.0000000000000000E+0	
# Delta_X	1.000000	1.000000	
# ***End_of_Header***			
# X_Value	Untitled	Untitled 1	Comment
#
# set 2--
# LabVIEW Measurement	
# Writer_Version	2
# Reader_Version	2
# Separator	Tab
# Decimal_Separator	.
# Multi_Headings	No
# X_Columns	One
# Time_Pref	Relative
# Operator	Methods Students
# Description	Don't delete initial header
# Date	2015/09/23
# Time	14:23:21.3099026679992675781
# ***End_of_Header***	
	
# Channels	2		
# Samples	1	1	
# Date	1903/12/31	1903/12/31	
# Time	18:00:00	18:00:00	
# X_Dimension	Time	Time	
# X0	0.0000000000000000E+0	0.0000000000000000E+0	
# Delta_X	1.000000	1.000000	
# ***End_of_Header***			
# X_Value	Untitled	Untitled 1	Comment

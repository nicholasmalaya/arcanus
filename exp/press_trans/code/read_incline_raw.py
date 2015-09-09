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
path="../data/alldata_incl.lvm"
file = open(path, "r+")

#
# data objects
#
set_names=[]

for line in file:
    #
    # sep by whitespace
    #
    line_list = line.split()

    if( len(line_list) > 2):
        #
        # reset! save name of this set
        #
        set_name=line_list[2:]
        set_names.append(' '.join(set_name))
        
        

    else:
        b=1

#
# clean up
#
file.close()       

#
# steady as she goes
#
sys.exit(0)

#
# nick 
# 9/9/15
#

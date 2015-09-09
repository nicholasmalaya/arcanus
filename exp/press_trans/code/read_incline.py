#!/bin/py
#
# open file
# read contents
# (re)start when third column found
#
path="../data/alldata_incl.lvm"
file = open(path, "r+")

for line in file:

    line_list = line.split()

    #
    # reset!
    #
    if( len(line_list) > 2):
        set_name=line_list[2:]
        print set_name
        

#
# nick 
# 9/9/15
#

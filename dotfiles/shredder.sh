#!/bin/bash
#
# set in crontab to 'shred on the 5s'!
#
comm=(shred rm)
fls=(pass pass~ pass.gpg~ \#pass\# low_sec~ shredder.sh~)

for item in ${comm[*]}
do
    for fl in ${fls[*]}
    do
    $item $fl
    done
done

#
# nick 
# SHREDDER MKII
# 5/4/15
#
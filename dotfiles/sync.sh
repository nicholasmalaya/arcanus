#!/bin/bash
#
# sync dot files on magus with central repo


diff /h2/nick/.emacs ./emacs
if [ $? neq 0 ]
then
    cp /h2/nick/.emacs emacs
    git commit emacs -m '[paleologos]: Diff detected in .emacs. Automatically sync initialized.'
fi
#
# nick
# 2/28/14
#
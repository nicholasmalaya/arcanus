#!/bin/bash
#
# sync dot files on magus with central repo

manus()
{ # take input string, test if changed
diff /h2/nick/".$1" ./"$1"
if [ $? -ne 0 ]
then
    cp /h2/nick/".$1" "$1"
    git commit "$1" -m "[paleologos]: Diff detected in $1. Automatically sync initialized."
    git push
fi
}

manus emacs
manus bashrc
manus aliases

#
# now, diff crontab
#
crontab -l | diff blah -
if [ $? -ne 0 ]
then
    crontab -l > cron
    git commit cron -m "[paleologos]: Diff detected in cron. Automatically sync initialized."
    git push
fi

#
# nick
# 2/28/14
#
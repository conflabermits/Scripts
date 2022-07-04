#!/bin/bash
# An alternative to brew installing tree
# Source: https://superuser.com/questions/359723/mac-os-x-equivalent-of-the-ubuntu-tree-command

#SEDMAGIC='s;[^/]*/;|____;g;s;____|; |;g'
SEDMAGIC='s;[^/]*/;|-- ;g;s;-- |;   |;g'

if [ "$#" -gt 0 ] ; then
   dirlist="$@"
else
   dirlist="."
fi

for x in $dirlist; do
     find "$x" -print | sed -e "$SEDMAGIC"
done

# Custom profile specifically for WSL bash

echo ".bash_profile loaded"
. ~/.profile
clear
echo "Welcome `whoami` to `hostname`"
echo

alias cds='cd /local/git/Scripts'

#!/bin/bash

# Uses the Mac say command to speak via the speakers
# Mostly just for testing out bash command syntax

if [ $(uname) == "Darwin" ] ; then
	echo
else
	echo "This script works best on Mac OS X!"
	echo "Exiting script!"
	exit
fi

echo "What would you like me to say?"
read userInput

say $userInput

echo


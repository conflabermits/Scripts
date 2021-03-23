#!/bin/bash

workingDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "We're up all night to get busy!"

while [ 1=1 ]
do
	$workingDir/dictionaryChecker.sh
	sleep 2
	$workingDir/randProgress.sh
	sleep 2
	$workingDir/fastProgress.sh
	sleep 2
	$workingDir/showProc.sh
	sleep 2
	$workingDir/slowProgress.sh
	sleep 2
	$workingDir/rapidProgress.sh
	sleep 2
	echo
done


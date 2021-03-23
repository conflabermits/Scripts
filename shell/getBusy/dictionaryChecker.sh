#!/bin/bash

workingDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Checking local dictionary to verify existence of words against remote dictionary"
sleep 1

i=0
while [ $i -lt 20 ]; do
	rand=$(( $RANDOM % 20 ))
	word=$($workingDir/rand.sh $workingDir/words.txt)
	if [ $rand -eq 19 ]; then
		echo "Checking for word \"$word\" in local dictionary... word \"$word\" NOT found."
		sleep 0.5
		echo "Adding word \"$word\" to local dictionary from remote dictionary."
	else
		echo "Checking for word \"$word\" in local dictionary... word \"$word\" found."
	fi
	let i=i+1
	sleep 1
done

 
#you could even use other languages. Importing spanish support, etc
 

echo "Dictionary does not contain enough tildes. Adding more tildes to toner file."

echo "Done!"
sleep 2

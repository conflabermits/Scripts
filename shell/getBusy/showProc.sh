#!/bin/bash

echo "Adding processes to execution cycle"
echo
sleep 5
echo "Priortizing process list by heuristic workload algorithm"
echo 
sleep 5
ps -ef | grep -v chrome | grep -v getBusy | grep -v showProc
echo "-------------------------"
echo "Done!"
sleep 2

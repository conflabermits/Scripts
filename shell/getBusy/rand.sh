#!/bin/bash
file=$1
total=$(cat $file | wc -l)
rand=$(( $RANDOM % $total ))
rand=$(( $rand + 1))
cat $file | head -$rand | tail -1

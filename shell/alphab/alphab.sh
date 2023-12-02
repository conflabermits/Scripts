#!/bin/bash

echo && echo "$*" | sed 's/ /\n/g' | sort -f | sed 's/$/ /g' | tr -d '\n' && echo



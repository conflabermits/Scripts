#!/bin/bash

user="$1"
ip="$2"
remotePath="$3"
localPath="$4"

sshfs $user@$ip:$remotePath $localPath

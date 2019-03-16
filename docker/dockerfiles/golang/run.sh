#!/bin/bash

docker run \
    --tty \
    --interactive \
    --name=golang \
    --hostname=golang \
    local/golang

docker rm golang


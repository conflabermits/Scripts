#!/bin/bash

docker run \
    --tty \
    --interactive \
    --name=python-2 \
    --hostname=python-2 \
    local/python:2

docker rm python-2


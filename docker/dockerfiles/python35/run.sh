#!/bin/bash

docker run \
    --tty \
    --interactive \
    --name=python-3 \
    --hostname=python-3 \
    local/python:3

docker rm python-3


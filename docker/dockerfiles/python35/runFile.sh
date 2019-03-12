#!/bin/bash

case `file -L "$1" 2>&1` in
    *"Python script"*)
        ;;
    *)
        echo "Usage: $0 /path/to/file.py [args]"
        exit 1
        ;;
esac

docker run \
    --net=host \
    -v "$1":"/tmp/file.py" \
    --interactive \
    --tty \
    --detach \
    --name=python-3-runner \
    --hostname=python-3-runner \
    local/python:3

docker exec python-3-runner /usr/bin/python3 /tmp/file.py "${@:2}"

docker stop \
    python-3-runner

docker rm \
    python-3-runner


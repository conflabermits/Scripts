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
    --name=python-2-runner \
    --hostname=python-2-runner \
    local/python:2

docker exec python-2-runner /usr/bin/python2.7 /tmp/file.py "${@:2}"
    #--interactive \
    #--tty \
    #python-2-runner /usr/bin/python2.7 /tmp/file.py
    #"$@"

docker stop \
    python-2-runner

docker rm \
    python-2-runner


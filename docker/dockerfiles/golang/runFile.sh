#!/bin/bash

case `file -L "$1" 2>&1` in
    *"C source, ASCII text"*)
        ;;
    *)
        echo "Usage: $0 /path/to/file.go [args]"
        exit 1
        ;;
esac

docker run \
    --net=host \
    --interactive \
    --tty \
    --detach \
    --name=go-runner \
    --hostname=go-runner \
    local/golang

docker cp \
    $1 \
    go-runner:/tmp/

docker exec go-runner /usr/bin/go run /tmp/$1 "${@:2}"

docker stop \
    go-runner

docker rm \
    go-runner


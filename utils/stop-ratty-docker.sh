#!/usr/bin/env bash
# Kills an already existing Rat Bot instance in Docker.

set -e -x

docker inspect --format="{{.State.Running}}" ratbot

if [ $? -eq 0 ]; then
    echo "ratbot exists, stopping in Docker..."
    docker stop ratbot
else
    echo "Error: ratbot isn't running in Docker."
    exit 1
fi
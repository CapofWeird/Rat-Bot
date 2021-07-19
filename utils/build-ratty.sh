#!/usr/bin/env bash
# This builds Rat Bot using the provided Dockerfile.

# Check if Docker exists.
if ! [ -x "$(command -v docker)" ]; then
    echo 'Error: Docker is not installed or is not in your PATH.' >&2
    exit 1
fi

echo "Building Rat Bot and tagging as ratbot/ratbot:latest."
set -e -x # Exit on error, print commands as run

docker build . -t ratbot/ratbot:latest
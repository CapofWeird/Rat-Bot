#!/usr/bin/env bash
# Run Rat Bot in the Docker container.
# This also checks if .env is present in the folder as we pass that for the token.

if ! [ -s ".env" ]; then
    echo "Error: .env file must be present. Run `cp .env.example .env` and put in your bot token." >&2
    exit 1
fi

echo "Running Rat Bot in Docker."
docker run --env-file .env -d --name "ratbot" ratbot/ratbot:latest
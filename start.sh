#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

# Clear any trapped python cache artifacts if needed
echo "Starting FastAPI Microservice..."

# Execute Uvicorn, replacing the shell script process with the server process
exec uvicorn main:app --host 0.0.0.0 --port "${PORT:-9000}" --workers 2
#!/bin/bash

set -e

if ! command -v python3 &>/dev/null; then
    echo "Python3 is not installed. Please install Python3."
    exit 1
fi

if [ ! -f secret.py ]; then
    cp secret.py.example secret.py
    echo "Please edit the secret.py file and add in your secrets."
    exit 1
fi

if [ ! -f database.db ]; then
    echo "A database file was not found."
    echo "Auto-generating a database file."
    python3 database.py
fi

python3 app.py

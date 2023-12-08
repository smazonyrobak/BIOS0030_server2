#!/bin/bash

# Start Voilà in the background
voila --no-browser --port=8866 --show_tracebacks=True --VoilaConfiguration.file_allowlist='^.*\.(ipynb|png|jpg|gif|svg|json|csv)$' &

# Set the FLASK_APP environment variable
export FLASK_APP=flask_framework.py

# Start Flask in the foreground
flask run --host=0.0.0.0 --port=8000

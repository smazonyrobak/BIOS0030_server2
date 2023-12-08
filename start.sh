#!/bin/bash

# Start Voilà in the background
voila --no-browser --port=8866 All_tests_launcher/All_tests_launcher.ipynb &

# Start Flask in the foreground
flask run --host=0.0.0.0 --port=8000

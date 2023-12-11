#!/bin/bash

# Activate the virtual environment
source /root/BIOS0030_server2/BIOS0030_environment/bin/activate

# Start Voila with the specified options
voila --no-browser \
      --port=8866 \
      --show_tracebacks=True \
      --VoilaConfiguration.file_allowlist='^.*\.(ipynb|png|jpg|gif|svg|json|csv)$' &

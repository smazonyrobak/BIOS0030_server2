#!/bin/bash

# Start Voilà in the background
voila --no-browser &

# Wait for Voilà to start
sleep 1

# Open the notebook in the default web browser
open http://localhost:8866/voila/render/All_Tests_Launcher/All_Tests_Launcher.ipynb

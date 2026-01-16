#!/bin/bash

# Sample shell script for demonstration of running a Python metrics collection script

# Path to your Python executable
PYTHON=/usr/bin/python3

# Path to your Python script (replace with your own)
SCRIPT_PATH=/path/to/your/project/script/sample.py

# Path to your logs folder (replace with your own)
LOG_DIR=/path/to/your/project/logs

# Ensure log folder exists
mkdir -p $LOG_DIR

# Run the Python script
$PYTHON $SCRIPT_PATH >> $LOG_DIR/success.log 2>> $LOG_DIR/error.log

# Explanation:
# - Standard output (success messages) are appended to logs/success.log
# - Error messages are appended to logs/error.log

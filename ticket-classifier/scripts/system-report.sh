#!/bin/bash

case "${1:-}" in
    --help|-h)
        echo "Display a system report with date, user, disk usage, and memory usage."
        echo "Usage: $0 [--help|-h]"
        echo "Options:"
        echo "    --help, -h    Show this help message and exit."
        exit 0
        ;;
esac

echo "=== System Report ==="
echo "Date: $(date)"
echo "User: $USER"
echo "--------------------"

# Display Disk Usage
echo "Disk Usage:"
df -h | grep '^/dev/'

# Display Memory Usage
echo "Memory Usage:"
free -h

# INTENTIONAL BUG/IMPROVEMENT NEEDED BELOW:
# This line tries to show the script version, but the variable isn't defined!
echo "Script Version: $VERSION" 

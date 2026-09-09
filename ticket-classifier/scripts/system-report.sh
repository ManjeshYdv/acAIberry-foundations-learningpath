#!/usr/bin/env bash

echo "System Report"
echo "============="

echo
echo "Date:"
date

echo
echo "User:"
whoami

echo
echo "Host:"
hostname

echo
echo "Project size:"
du -sh .

echo
echo "Disk usage:"
df -h .

echo
echo "Memory usage:"
free -h

echo
echo "Top 5 processes by memory usage:"
ps aux --sort=-%mem | head -n 6

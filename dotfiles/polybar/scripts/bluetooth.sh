#!/bin/bash

# Connected bluetooth devices
MACS=$(hcitool con | grep -o '[[:xdigit:]:]\{11,17\}' | tr " " "\n")

if [ -z "$MACS" ]
    then
    echo "Not connected"
else
    echo "Connected"
fi

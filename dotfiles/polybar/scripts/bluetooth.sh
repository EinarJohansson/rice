#!/bin/bash

# Connected bluetooth devices
MACS=$(hcitool con | grep -o '[[:xdigit:]:]\{11,17\}' | tr " " "\n")

if [ -z "$MACS" ]
    then
    echo "%{F#7a7873}"
else
    echo "%{F#555}"
fi

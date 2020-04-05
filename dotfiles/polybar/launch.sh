#!/bin/bash

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch Polybar, using default config location ~/.config/polybar/config
echo "---" | tee -a /tmp/polybar1.log /tmp/polybar2.log
polybar middle >>/tmp/polybar1.log 2>&1 &
polybar misc >>/tmp/polybar2.log 2>&1 &
polybar system >> /tmp/polybar3.log 2>&1 &

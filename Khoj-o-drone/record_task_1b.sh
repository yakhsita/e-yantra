#!/usr/bin/env bash
# Run in a ROS-sourced terminal; stop with Ctrl+C after 60+ seconds.
set -e
cd "$HOME/pico_ws"
echo "Recording /pos_error and /whycode_node/markers. Stop with Ctrl+C after at least 60 seconds."
ros2 bag record -o task_1b /pos_error /whycode_node/markers

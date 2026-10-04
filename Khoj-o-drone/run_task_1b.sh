#!/usr/bin/env bash
# Use separate terminals for each process; this script prints the commands.
cat <<'EOF'
Terminal 1 — simulation:
source /opt/ros/humble/setup.bash
source ~/pico_ws/install/setup.bash
ros2 launch swift_pico swift_pico_simulation.launch.py

Terminal 2 — controller:
source /opt/ros/humble/setup.bash
source ~/pico_ws/install/setup.bash
ros2 run swift_pico task_1b_controller

Terminal 3 — PID tuner:
source /opt/ros/humble/setup.bash
source ~/pico_ws/install/setup.bash
ros2 launch pid_tune pid_tune_drone.launch.py

Monitor throttle error:
ros2 topic echo /pos_error
EOF

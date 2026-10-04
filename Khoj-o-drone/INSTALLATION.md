# Task 1B — Installation and Run Guide

## Environment
- Ubuntu 22.04 LTS
- ROS 2 Humble
- Workspace used: `~/pico_ws`
- Task 0 prerequisites and official Khoj-O-Drone simulation packages installed

## 1. Obtain official source
Use the official e-Yantra Khoj-O-Drone repository and the competition-specified branch/version. This companion repo contains notes/scripts only, not the official simulator or controller source.

## 2. Update and build
```bash
cd ~/pico_ws/src
git pull
cd ~/pico_ws
colcon build
source install/setup.bash
```
If the official repository instructions require recursive submodules or a fresh clone, follow those instructions.

## 3. Source each terminal
```bash
source /opt/ros/humble/setup.bash
source ~/pico_ws/install/setup.bash
```

## 4. Terminal 1 — simulation
```bash
ros2 launch swift_pico swift_pico_simulation.launch.py
```

## 5. Terminal 2 — controller
```bash
ros2 run swift_pico task_1b_controller
```
When prompted, answer `Y` if using the live PID tuner. Keep the controller running.

## 6. Terminal 3 — PID tuner
```bash
ros2 launch pid_tune pid_tune_drone.launch.py
```
Set the throttle gains listed in `PID_GAINS.md`. The tuner GUI need not be shown in the video if the task instructions say it is not required.

## 7. Validate throttle error
In another sourced terminal:
```bash
ros2 topic echo /pos_error
```
Watch `throttle_error`. Confirm it enters [-0.4, +0.4] within 5 seconds and remains there for 10 seconds. A few in-range samples alone do not prove settling.

## 8. Record rosbag
From a sourced terminal:
```bash
cd ~/pico_ws
ros2 bag record -o task_1b /pos_error /whycode_node/markers
```
Record at least 60 seconds, then press `Ctrl+C`.

Inspect:
```bash
ros2 bag info task_1b
ls -lh task_1b
```
Expected files include `task_1b_0.db3` and `metadata.yaml`.

## 9. Create the submission ZIP
Replace team ID if needed:
```bash
cd ~/pico_ws/task_1b
zip -r ../KD_3316_task_1b.zip task_1b_0.db3 metadata.yaml
unzip -l ~/pico_ws/KD_3316_task_1b.zip
```
Submit the ZIP and required video using your team's process. Retain the original bag files until upload is confirmed.

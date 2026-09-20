# e-Yantra Khoj-O-Drone — Quick Commands for Future Tasks

This file contains only the important commands and terminal arrangements we are likely to reuse.

---

## 1. Every new ROS 2 terminal

Start with:

```bash
source /opt/ros/humble/setup.bash
```

Then source the workspace you are using.

### Turtlesim

```bash
source ~/turtlesim_ws/install/setup.bash
```

### MuJoCo

```bash
source ~/pico_mujoco_ws/install/setup.bash
```

The MuJoCo workspace was also added to `.bashrc`, so new terminals may already have it sourced.

If something is not recognized, manually run the `source` command.

---

# 2. Turtlesim — 2 terminals

Use **2 terminals**, preferably side by side.

### Terminal 1 — Turtlesim

```bash
source /opt/ros/humble/setup.bash
source ~/turtlesim_ws/install/setup.bash
ros2 run turtlesim turtlesim_node
```

Keep this terminal running.

### Terminal 2 — Your program

```bash
source /opt/ros/humble/setup.bash
source ~/turtlesim_ws/install/setup.bash
ros2 run kd_task_0 task_0
```

If the simulation/program is running, leave its terminal alone and use another terminal for the next command.

---

# 3. MuJoCo Swift Pico — 2 terminals

### Terminal 1 — Simulation

```bash
source /opt/ros/humble/setup.bash
source ~/pico_mujoco_ws/install/setup.bash
ros2 launch swift_pico swift_pico_simulation.launch.py
```

Keep this terminal running while the simulation is needed.

### Terminal 2 — Commands/testing

```bash
source /opt/ros/humble/setup.bash
source ~/pico_mujoco_ws/install/setup.bash
```

Then run whatever command the current task requires.

---

# 4. Build after changing ROS 2 code

### Turtlesim

```bash
cd ~/turtlesim_ws
colcon build
source ~/turtlesim_ws/install/setup.bash
```

### MuJoCo

```bash
cd ~/pico_mujoco_ws
colcon build
source ~/pico_mujoco_ws/install/setup.bash
```

Remember:

**edit → build → source → run**

---

# 5. Evaluator

Task 0:

```bash
eyantra-autoeval evaluate --year 2026 --theme KD --task 0
```

For another task, change the task number according to the competition instructions:

```bash
eyantra-autoeval evaluate --year 2026 --theme KD --task <TASK_NUMBER>
```

---

# 6. Useful ROS 2 commands

See running nodes:

```bash
ros2 node list
```

See topics:

```bash
ros2 topic list
```

See topic information:

```bash
ros2 topic info /topic_name
```

See messages from a topic:

```bash
ros2 topic echo /topic_name
```

Example:

```bash
ros2 topic echo /turtle1/pose
```

---

# 7. Important locations

### Turtlesim workspace

```text
~/turtlesim_ws
```

Our package:

```text
~/turtlesim_ws/src/kd_task_0
```

Our Python file:

```text
~/turtlesim_ws/src/kd_task_0/kd_task_0/task_0.py
```

### MuJoCo workspace

```text
~/pico_mujoco_ws
```

Source folder:

```text
~/pico_mujoco_ws/src
```

---

# 8. Terminal layout

## Turtlesim

```text
┌──────────────────────┬──────────────────────┐
│ TERMINAL 1           │ TERMINAL 2           │
│                      │                      │
│ turtlesim_node       │ your program         │
│                      │                      │
│ simulation           │ task/program         │
└──────────────────────┴──────────────────────┘
```

## MuJoCo

```text
┌──────────────────────┬──────────────────────┐
│ TERMINAL 1           │ TERMINAL 2           │
│                      │                      │
│ MuJoCo simulation    │ commands / testing   │
│                      │                      │
│ ros2 launch ...      │ task commands        │
└──────────────────────┴──────────────────────┘
```

They do not have to be physically side by side. Side-by-side is just easier when you need to watch the simulation and type commands at the same time.

---

# 9. Most important habit

If a simulation or ROS 2 node is running:

**Leave that terminal running.**

Open another terminal for the next command.

To stop a running program:

```text
Ctrl+C
```

Do **not** use:

```text
Ctrl+Z
```

---

# 10. Simple workflow to remember

```text
1. Open terminal
2. source ROS 2
3. source the correct workspace
4. Start simulation/node
5. Open another terminal
6. source ROS 2 + workspace
7. Run the task/program
8. If code changed: build → source → run
9. Stop programs with Ctrl+C
```

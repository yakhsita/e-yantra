
# e-Yantra Khoj-O-Drone — Bonus Task 

This README records the bonus task.


## 1. Turtlesim Workspace

Created:

```bash
cd
mkdir -p turtlesim_ws/src
```

Cloned the `turtle_sim` branch:

```bash
cd ~/turtlesim_ws/src
git clone -b turtle_sim https://github.com/eYantra-Robotics-Competition/eYRC_26-27_Khojo-Drone.git
```

Build:

```bash
cd ~/turtlesim_ws
colcon build
```

Source:

```bash
source ~/turtlesim_ws/install/setup.bash
```

### Created Task 0 package

```bash
cd ~/turtlesim_ws/src
ros2 pkg create --build-type ament_python kd_task_0
```

Created the Python program:

```bash
cd ~/turtlesim_ws/src/kd_task_0/kd_task_0
touch task_0.py
chmod +x task_0.py
```

The program:

1. Moves the turtle to the required starting position.
2. Turns the turtle upward.
3. Draws a circle of diameter 2.0.
4. Moves the turtle to `(5.0, 5.0)`.
5. Stops.

For the circle:

```text
linear velocity = 1.0
angular velocity = 1.0
radius = v / w = 1.0
diameter = 2.0
```

### Package configuration

`setup.py` contains:

```python
entry_points={
    'console_scripts': [
        'task_0 = kd_task_0.task_0:main',
    ],
},
```

`package.xml` contains:

```xml
<depend>rclpy</depend>
<depend>geometry_msgs</depend>
<depend>turtlesim</depend>
```

After changes:

```bash
cd ~/turtlesim_ws
colcon build
source ~/turtlesim_ws/install/setup.bash
```

### Turtlesim test

Terminal 1:

```bash
source /opt/ros/humble/setup.bash
source ~/turtlesim_ws/install/setup.bash
ros2 run turtlesim turtlesim_node
```

Terminal 2:

```bash
source /opt/ros/humble/setup.bash
source ~/turtlesim_ws/install/setup.bash
ros2 run kd_task_0 task_0
```

The turtle successfully ran the program.

---

## 2. MuJoCo Swift Pico Workspace

Created:

```bash
cd ~
mkdir -p pico_mujoco_ws/src
```

Cloned the `kd_sim` branch recursively:

```bash
cd ~/pico_mujoco_ws/src
git clone -b kd_sim https://github.com/eYantra-Robotics-Competition/eYRC_26-27_Khojo-Drone.git --recursive .
```

### Missing `actuator_msgs`

The first build:

```bash
cd ~/pico_mujoco_ws
colcon build
```

failed because `actuator_msgs` was missing.

Installed:

```bash
sudo apt install ros-humble-actuator-msgs
```

Then rebuilt:

```bash
cd ~/pico_mujoco_ws
colcon build
```

Result: 17 packages finished successfully.

### Workspace sourcing

Added MuJoCo workspace to `.bashrc`:

```bash
echo "source ~/pico_mujoco_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

---

## 3. Missing `image_view`

First simulation launch:

```bash
ros2 launch swift_pico swift_pico_simulation.launch.py
```

reported that `image_view` was missing.

Installed:

```bash
sudo apt install ros-humble-image-view
```

---

## 4. MuJoCo shared-library fix

The next error was:

```text
libmujoco.so.3.9.0: cannot open shared object file
```

Found the Python MuJoCo location:

```bash
python3 -c "import mujoco, os; print(os.path.dirname(mujoco.__file__))"
```

It returned:

```text
/home/yakhsita/.local/lib/python3.10/site-packages/mujoco
```

Confirmed the library:

```bash
ls -l /home/yakhsita/.local/lib/python3.10/site-packages/mujoco/libmujoco.so.3.9.0
```

Added the library directory:

```bash
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/yakhsita/.local/lib/python3.10/site-packages/mujoco' >> ~/.bashrc
source ~/.bashrc
```

Verified:

```bash
ldd ~/pico_mujoco_ws/install/swift_pico/lib/swift_pico/mujoco_bridge | grep mujoco
```

It correctly found:

```text
libmujoco.so.3.9.0 => /home/yakhsita/.local/lib/python3.10/site-packages/mujoco/libmujoco.so.3.9.0
```

---

## 5. Missing GLFW library

Running the bridge revealed:

```text
libglfw.so.3: cannot open shared object file
```

Installed:

```bash
sudo apt install libglfw3
```

After this, the MuJoCo simulation window opened successfully.

The bridge showed:

```text
=== Swift Pico MuJoCo -- ROS2 Bridge ===
Camera:  /image_raw
Info:    /camera_info
Markers: /whycode_node/markers
```

and:

```text
[DISARMED]rpm=[0 0 0 0]
```

This confirmed that the Swift Pico MuJoCo simulation can start.

---

## 6. Final Task 0 Environment Check

Ran:

```bash
eyantra-autoeval evaluate --year 2026 --theme KD --task 0
```

Final result:

```text
ROS2 humble is succesfully installed on this system.
MuJoCo is succesfully installed on this system.
ros-humble-desktop is succesfully installed on this system.
Khoj-O-Drone is geared up and ready to take flight ;)...
```

## Status

**Task 0 environment/setup: READY ✅**

This README records the setup and verification. Future competition tasks may require additional packages, code, builds, or evaluation.

---

## 7. Important rule

If a ROS 2 simulation is running, stop it with:

```text
Ctrl+C
```

Do **not** use `Ctrl+Z`.

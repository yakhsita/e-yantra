# e-Yantra Task 0 — Ubuntu, ROS 2 Humble & MuJoCo Setup

This README explains **what we installed, why we installed it, and what the important commands did**.

---

## 1. Ubuntu 22.04

Ubuntu is the Linux operating system we are using for the e-Yantra project.

The e-Yantra setup uses **Ubuntu 22.04 (Jammy)** because ROS 2 Humble is supported on it.

Think of it as:

> **Ubuntu = the operating system on which all our robotics software runs.**

---

# 2. Setting the Locale

### Commands

```bash
locale
sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

### What is a locale?

A locale tells Ubuntu how to handle things such as:

- language
- characters
- numbers
- dates
- text encoding

ROS 2 expects a **UTF-8 compatible locale**.

### Simple idea

> **Locale = telling Ubuntu how to correctly understand and display text.**

We configured:

```text
en_US.UTF-8
```

---

# 3. `apt` and Updating Ubuntu

We used:

```bash
sudo apt update
sudo apt upgrade
```

### What is `apt`?

`apt` is Ubuntu's **package manager**.

A package is basically a piece of software that Ubuntu can install/manage.

### `apt update`

```bash
sudo apt update
```

Downloads the latest information about available software.

It does **not** normally upgrade the software itself.

Think:

> "Check what software/packages are available and whether there are newer versions."

### `apt upgrade`

```bash
sudo apt upgrade
```

Actually upgrades installed packages when updates are available.

Think:

> `apt update` = check for updates  
> `apt upgrade` = install the updates

---

# 4. `sudo`

We repeatedly used commands such as:

```bash
sudo apt install ...
```

`sudo` means:

> "Run this command with administrator privileges."

Installing system software requires administrator permission.

Ubuntu will therefore ask for your password.

---

# 5. Ubuntu Universe Repository

We installed:

```bash
sudo apt install software-properties-common
```

and enabled:

```bash
sudo add-apt-repository universe
```

### What is a repository?

A repository is basically a **software store/server containing packages** that Ubuntu can download.

Ubuntu has different repositories/categories.

### What is `universe`?

The **Universe repository** contains a very large collection of community-maintained/open-source software that is not part of Ubuntu's core system.

Some software and dependencies needed by robotics/development tools are available through these repositories.

So we enabled it because the ROS installation may need packages from it.

### Simple idea

> **Universe = another Ubuntu software shelf containing lots of additional packages.**

---

# 6. `curl`

We installed:

```bash
sudo apt install curl -y
```

### What is curl?

`curl` is a command-line program used to **communicate with websites/servers and download data**.

We used it to obtain information about the ROS 2 repository package.

For example, this command contacted GitHub:

```bash
curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest
```

### Simple idea

> **curl = a tool that lets the terminal communicate with the internet.**

It is similar to using a browser, except it works from the command line.

---

# 7. ROS 2 Repository

We installed:

```text
ros2-apt-source
```

using the downloaded `.deb` file.

### Why?

Ubuntu's normal software repositories don't automatically contain everything needed for ROS 2 Humble.

We therefore added the official ROS 2 package repository.

After that:

```bash
sudo apt update
```

showed:

```text
http://packages.ros.org/ros2/ubuntu jammy/main
```

This confirmed that Ubuntu could access the ROS 2 repository.

### Simple idea

> **ROS repository = the software store from which Ubuntu gets ROS 2 packages.**

---

# 8. ROS 2 Humble

We installed:

```bash
sudo apt install ros-humble-desktop
```

This installed the **ROS 2 Humble Desktop** distribution.

## What is ROS 2?

ROS stands for:

> **Robot Operating System**

Despite the name, ROS is not actually an operating system like Windows or Ubuntu.

It is a **robotics software framework**.

It provides tools that allow different programs in a robot system to communicate with each other.

---

## Example

Imagine our drone has separate programs:

```text
Camera
   ↓
Image Processing
   ↓
Drone Detection
   ↓
Drone Tracking
   ↓
Navigation / Control
```

Instead of putting everything into one giant program, these can be separate ROS 2 **nodes**.

ROS 2 provides the communication system between them.

For example:

```text
Camera Node
     |
     | image data
     ↓
ROS 2
     |
     ↓
Detection Node
     |
     | detected drone
     ↓
Tracking Node
```

### Simple idea

> **ROS 2 = a framework that helps different parts/programs of a robot communicate and work together.**

---

# 9. Why did we run the Talker/Listener test?

We ran:

### Terminal 1

```bash
ros2 run demo_nodes_cpp talker
```

### Terminal 2

```bash
ros2 run demo_nodes_py listener
```

The talker published:

```text
Hello World
```

The listener received it.

Conceptually:

```text
TALKER
  |
  | "Hello World"
  ↓
ROS 2 communication
  |
  ↓
LISTENER
```

This verified that our ROS 2 installation and communication system were working.

---

# 10. ROS Development Tools

We installed:

```bash
sudo apt install ros-dev-tools
```

These are tools used when **developing/building ROS packages**.

They include tools such as:

- Git
- colcon
- ROS build tools
- package/development utilities

### What is `colcon`?

`colcon` is commonly used to **build ROS 2 packages/workspaces**.

For example, later in robotics projects we may have:

```text
ROS workspace
   ↓
source code
   ↓
colcon build
   ↓
built ROS packages
```

### Simple idea

> **ros-dev-tools = the toolbox used to develop ROS programs.**

---

# 11. `.bashrc` and ROS Environment

We added:

```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
```

and then:

```bash
source ~/.bashrc
```

### What is `setup.bash`?

ROS 2 has environment information that tells the terminal where ROS is installed and where its commands/packages are located.

This command:

```bash
source /opt/ros/humble/setup.bash
```

loads that information into the current terminal.

### Why put it in `.bashrc`?

`.bashrc` is a file that is automatically read when a new Bash terminal starts.

So adding:

```bash
source /opt/ros/humble/setup.bash
```

to `.bashrc` means:

> "Every time I open a terminal, automatically set up ROS 2."

That's why:

```bash
echo $ROS_DISTRO
```

gave:

```text
humble
```

### Simple idea

> **`.bashrc` = startup instructions for your terminal.**

---

# 12. MuJoCo

We installed:

```bash
pip3 install mujoco==3.9.0
```

### What is MuJoCo?

MuJoCo means:

> **Multi-Joint dynamics with Contact**

It is a **physics simulation engine**.

It can simulate things such as:

- gravity
- movement
- joints
- collisions
- forces
- robot dynamics

Instead of testing everything on a real robot immediately, we can test things in a simulated environment.

### Simple comparison

```text
ROS 2
  =
Robot software + communication

MuJoCo
  =
Physics simulation
```

---

# 13. Python

We checked:

```bash
python3 --version
```

and got:

```text
Python 3.10.12
```

Python is a programming language heavily used in robotics, computer vision, automation, and ROS 2.

---

# 14. pip

We checked:

```bash
pip3 --version
```

`pip` is Python's package manager.

It lets us install Python libraries.

For example:

```bash
pip3 install mujoco==3.9.0
```

means:

> "Use pip to install MuJoCo version 3.9.0."

---

# 15. NumPy

We installed:

```bash
pip3 install numpy
```

NumPy is used for **numerical calculations and arrays**.

For robotics/computer vision, we often work with:

- matrices
- coordinates
- vectors
- numerical data
- image data

### Simple idea

> **NumPy = fast numerical calculations in Python.**

---

# 16. SciPy

We installed:

```bash
pip3 install scipy
```

SciPy provides additional scientific and mathematical tools.

It is built on top of NumPy.

### Simple idea

> **SciPy = extra scientific/math tools for Python.**

---

# 17. OpenCV

We installed:

```bash
pip3 install opencv-python
```

OpenCV stands for:

> **Open Source Computer Vision Library**

It is used for processing images and video.

For example:

```text
Camera
  ↓
Image
  ↓
OpenCV
  ↓
Image processing
  ↓
Object detection/tracking
```

For a drone project, computer vision can be extremely useful.

### Simple idea

> **OpenCV = tools for working with camera images and video.**

---

# 18. Pillow

We installed:

```bash
pip3 install Pillow
```

Pillow is a Python library for working with images.

It can perform tasks such as:

- opening images
- saving images
- resizing images
- converting image formats
- basic image manipulation

### Simple idea

> **Pillow = Python's image-handling toolbox.**

---

# 19. MuJoCo Verification

We ran a Python command that:

1. Imported MuJoCo
2. Created a tiny simulation model
3. Created simulation data
4. Performed a physics simulation step
5. Printed the MuJoCo version

The expected output was:

```text
MuJoCo is working! Version: 3.9.0
```

This verifies that MuJoCo isn't merely installed — it can actually **load a model and perform a simulation step**.

---

# 20. What We Have Now

Our setup can be visualized as:

```text
                  UBUNTU 22.04
                       |
          +------------+------------+
          |                         |
        ROS 2                    Python
          |                         |
      ROS Humble              Python packages
          |                    /   |   |   \
          |                NumPy SciPy OpenCV Pillow
          |
   Robot communication
          |
       ROS Nodes
          |
          +-------------------+
                              |
                           MuJoCo
                              |
                       Physics simulation
```

Or, even simpler:

```text
Ubuntu
  ↓
The computer's operating system

ROS 2
  ↓
Lets robot programs communicate

MuJoCo
  ↓
Simulates robot physics

Python libraries
  ↓
Help with math + images + scientific processing
```

---

# 21. Installation Status

| Component | Status |
|---|---|
| Ubuntu 22.04 | ✅ |
| UTF-8 Locale | ✅ |
| Universe repository | ✅ |
| ROS 2 repository | ✅ |
| ROS 2 Humble Desktop | ✅ |
| ROS development tools | ✅ |
| ROS environment | ✅ |
| Talker/Listener test | ✅ |
| Python 3.10 | ✅ |
| MuJoCo 3.9.0 | ✅ |
| NumPy | ✅ |
| SciPy | ✅ |
| OpenCV | ✅ |
| Pillow | ✅ |
| MuJoCo verification | ✅ |

---

# 22. The Big Picture

The easiest way to remember all of this is:

> **Ubuntu is our base.**
>
> **ROS 2 helps the different robot programs communicate.**
>
> **MuJoCo gives us a virtual physics world.**
>
> **Python + NumPy/SciPy/OpenCV/Pillow give us programming, maths, and image-processing tools.**

These tools together form the software environment we need for the e-Yantra robotics tasks.

# Task 1A — Setup / Installation

## What Task 1A needs
- Ubuntu 22.04
- Python 3
- OpenCV
- NumPy
- Git
- e-Yantra `kd_sim` repository

The Task 1A image-processing script directly uses **OpenCV + NumPy**. ROS 2 is not directly used by this Python script.

## 1. Create workspace
```bash
mkdir -p ~/pico_ws/src
cd ~/pico_ws/src
git clone -b kd_sim https://github.com/eYantra-Robotics-Competition/eYRC_26-27_Khojo-Drone.git --recursive .
cd ~/pico_ws
colcon build
echo "source ~/pico_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

## 2. Install OpenCV and NumPy
```bash
sudo apt install python3-opencv python3-numpy
```

Check:
```bash
python3 -c "import cv2, numpy; print(cv2.__version__, numpy.__version__)"
```

Check ArUco:
```bash
python3 -c "import cv2; print(hasattr(cv2, 'aruco'))"
```
Expected: `True`

## 3. Go to Task 1A folder
```bash
cd ~/pico_ws/src/swift_pico/scripts
```

Important files:
```text
task1a.py             → main program
image_1.jpg           → input image
image_1_results.txt   → generated result
```

## 4. Run
```bash
python3 task1a.py --image image_1.jpg
```

Check the result:
```bash
cat image_1_results.txt
```

The result file is created in the same folder as the input image.

## Quick troubleshooting

OpenCV:
```bash
sudo apt install python3-opencv
```

NumPy:
```bash
sudo apt install python3-numpy
```

Wrong folder:
```bash
cd ~/pico_ws/src/swift_pico/scripts
```

Check files:
```bash
ls
```

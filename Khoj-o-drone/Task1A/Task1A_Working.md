# Task 1A — How It Works

## Goal
- **Red triangles** → Critical Survivors
- **Yellow circles** → Stable Survivors
- Black cuboids, green foliage and blue terrain → ignored

## Overall pipeline

```text
Input Image
    ↓
Detect ArUco markers
    ↓
Check IDs 80, 85, 90, 95
    ↓
Perspective transform
    ↓
900 × 900 straight arena
    ↓
Create 11 × 11 grid intersections
    ↓
Detect red regions → centres → nearest intersection
    ↓
Detect yellow regions → centres → nearest intersection
    ↓
Write results.txt
```

## 1. ArUco markers

Required corner marker IDs:

```text
80     85
┌─────────┐
│  ARENA  │
│         │
└─────────┘
95     90
```

If a required marker is missing, the program stops.

**Why?** The markers give the four corners of the playing field.

📷 **Add your ArUco/original image here.**

---

## 2. Perspective correction

The camera image can be tilted. The four arena corners are used to straighten it.

```text
Tilted image
     ↓
Perspective transform
     ↓
900 × 900 straight arena
```

The final arena contains only the playing field, not the corner markers.

📷 **Add your perspective-correction screenshot here.**

---

## 3. Grid

The arena has:

- 12 × 12 cells
- 11 × 11 internal intersections
- **121 intersections**
- Cell size = `900 / 12 = 75 pixels`

Labels:

```text
A1  B1  C1 ... K1
A2  B2  C2 ... K2
...
A11 B11 C11 ... K11
```

Top-left = **A1**  
Bottom-right = **K11**

📷 **Add your grid + labels screenshot here.**

---

## 4. Red detection

The image is converted to **HSV** and a red colour mask is created.

```text
Image
  ↓
HSV
  ↓
Red mask
  ↓
Contours
  ↓
Red survivor regions
```

Small regions are ignored.

---

## 5. Find survivor centre

OpenCV **image moments** are used:

```text
center_x = M10 / M00
center_y = M01 / M00
```

The code checks `M00 != 0` to avoid division by zero.

---

## 6. Find nearest intersection

The centre of each survivor is compared with all 121 grid intersections.

```text
Survivor ●

       •

            •  ← nearest intersection

                 •
```

The intersection with the smallest Euclidean distance is selected.

---

## 7. Yellow detection

Exactly the same process is used for yellow:

```text
HSV
 ↓
Yellow mask
 ↓
Contours
 ↓
Centres
 ↓
Nearest grid intersection
```

---

## 8. Final result

For the test image:

```text
Detected marker IDs: [80, 85, 90, 95]

Critical Survivors: C10, B7, I2
Stable Survivors: E9, H6, D2
```

Generated file:

```text
image_1_results.txt
```

📷 **Add your final debug-image screenshot here.**

---

## Important functions

| Function | Purpose |
|---|---|
| `cv2.imread()` | Load image |
| `cv2.aruco` | Detect ArUco markers |
| `cv2.getPerspectiveTransform()` | Calculate perspective correction |
| `cv2.warpPerspective()` | Straighten arena |
| `cv2.cvtColor()` | Convert to HSV |
| `cv2.inRange()` | Select a colour |
| `cv2.findContours()` | Find regions |
| `cv2.moments()` | Find centre |
| `argparse` | Accept `--image` |
| `Path()` | Create result-file path |

## The main logic to remember

```text
MARKERS
   ↓
Arena corners
   ↓
STRAIGHTEN
   ↓
900 × 900 arena
   ↓
GRID
   ↓
121 intersections
   ↓
COLOUR DETECTION
   ↓
Find centres
   ↓
Nearest intersection
   ↓
RESULTS FILE
```

## Suggested folder

```text
task1a/
├── task1a.py
├── image_1.jpg
├── image_1_results.txt
├── README_Task1A_Setup.md
├── README_Task1A_Working.md
└── images/
    ├── original.png
    ├── perspective_correction.png
    ├── grid_labels.png
    ├── final_debug.png
    └── terminal_result.png
```

## One-line summary

**Task 1A detects the four arena markers, straightens the arena, creates the grid, detects red/yellow survivors, finds their centres, maps them to the nearest grid intersections, and writes the locations to a results file.**

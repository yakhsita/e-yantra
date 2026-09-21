import argparse
import cv2
import numpy as np
from pathlib import Path


def main():

    # -----------------------------
    # Read command-line argument
    # -----------------------------
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    args = parser.parse_args()

    image = cv2.imread(args.image)

    if image is None:
        raise SystemExit(f"ERROR: Could not load image: {args.image}")


    # -----------------------------
    # Detect ArUco markers
    # -----------------------------
    dictionary = cv2.aruco.getPredefinedDictionary(
        cv2.aruco.DICT_4X4_250
    )

    parameters = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(dictionary, parameters)

    corners, ids, rejected = detector.detectMarkers(image)

    if ids is None:
        raise SystemExit("ERROR: No ArUco markers detected.")

    detected_ids = sorted(
        [int(marker_id) for marker_id in ids.flatten()]
    )

    required_ids = {80, 85, 90, 95}
    missing_ids = required_ids - set(detected_ids)

    if missing_ids:
        raise SystemExit(
            f"ERROR: Missing marker IDs: {sorted(missing_ids)}"
        )


    # -----------------------------
    # Get playing-field corners
    # -----------------------------
    field_corners = {}

    for marker_id, marker_corners in zip(ids.flatten(), corners):

        points = marker_corners[0]

        if marker_id == 80:
            field_corners[80] = points[0]

        elif marker_id == 85:
            field_corners[85] = points[1]

        elif marker_id == 90:
            field_corners[90] = points[2]

        elif marker_id == 95:
            field_corners[95] = points[3]


    # -----------------------------
    # Perspective transformation
    # -----------------------------
    src_points = np.float32([
        field_corners[80],
        field_corners[85],
        field_corners[90],
        field_corners[95]
    ])

    dst_points = np.float32([
        [0, 0],
        [899, 0],
        [899, 899],
        [0, 899]
    ])

    matrix = cv2.getPerspectiveTransform(
        src_points,
        dst_points
    )

    rectified = cv2.warpPerspective(
        image,
        matrix,
        (900, 900)
    )

    # Keep a clean copy for colour detection.
    # The grid will be drawn on 'rectified',
    # but detection will use this clean copy.
    detection_image = rectified.copy()


    # -----------------------------
    # Create 11 x 11 grid points
    # -----------------------------
    cell_size = 900 // 12

    grid_points = {}

    for row in range(11):

        for col in range(11):

            x = (col + 1) * cell_size
            y = (row + 1) * cell_size

            label = chr(ord('A') + col) + str(row + 1)

            grid_points[label] = (x, y)


    # -----------------------------
    # Convert clean image to HSV
    # -----------------------------
    hsv = cv2.cvtColor(
        detection_image,
        cv2.COLOR_BGR2HSV
    )


    # =========================================================
    # RED SURVIVORS
    # =========================================================

    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([179, 255, 255])

    mask_red1 = cv2.inRange(
        hsv,
        lower_red1,
        upper_red1
    )

    mask_red2 = cv2.inRange(
        hsv,
        lower_red2,
        upper_red2
    )

    red_mask = cv2.bitwise_or(
        mask_red1,
        mask_red2
    )

    red_contours, _ = cv2.findContours(
        red_mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    red_regions = [
        c for c in red_contours
        if cv2.contourArea(c) > 100
    ]


    # -----------------------------
    # Find red centers
    # -----------------------------
    red_centers = []

    for contour in red_regions:

        M = cv2.moments(contour)

        if M["m00"] != 0:

            center_x = int(
                M["m10"] / M["m00"]
            )

            center_y = int(
                M["m01"] / M["m00"]
            )

            red_centers.append(
                (center_x, center_y)
            )


    # -----------------------------
    # Assign red centers to grid
    # -----------------------------
    red_locations = []

    for center_x, center_y in red_centers:

        nearest_label = None
        nearest_distance = float("inf")

        for label, (grid_x, grid_y) in grid_points.items():

            distance = (
                (center_x - grid_x) ** 2
                +
                (center_y - grid_y) ** 2
            ) ** 0.5

            if distance < nearest_distance:

                nearest_distance = distance
                nearest_label = label

        red_locations.append(nearest_label)


    # =========================================================
    # YELLOW SURVIVORS
    # =========================================================

    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([40, 255, 255])

    yellow_mask = cv2.inRange(
        hsv,
        lower_yellow,
        upper_yellow
    )

    yellow_contours, _ = cv2.findContours(
        yellow_mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    yellow_regions = [
        c for c in yellow_contours
        if cv2.contourArea(c) > 100
    ]


    # -----------------------------
    # Find yellow centers
    # -----------------------------
    yellow_centers = []

    for contour in yellow_regions:

        M = cv2.moments(contour)

        if M["m00"] != 0:

            center_x = int(
                M["m10"] / M["m00"]
            )

            center_y = int(
                M["m01"] / M["m00"]
            )

            yellow_centers.append(
                (center_x, center_y)
            )


    # -----------------------------
    # Assign yellow centers to grid
    # -----------------------------
    yellow_locations = []

    for center_x, center_y in yellow_centers:

        nearest_label = None
        nearest_distance = float("inf")

        for label, (grid_x, grid_y) in grid_points.items():

            distance = (
                (center_x - grid_x) ** 2
                +
                (center_y - grid_y) ** 2
            ) ** 0.5

            if distance < nearest_distance:

                nearest_distance = distance
                nearest_label = label

        yellow_locations.append(nearest_label)


    # =========================================================
    # WRITE REQUIRED RESULTS FILE
    # =========================================================

    image_path = Path(args.image)

    results_path = image_path.with_name(
        image_path.stem + "_results.txt"
    )

    with open(results_path, "w") as f:

        f.write(
            f"Detected marker IDs: {detected_ids}\n"
        )

        f.write("\n")

        f.write(
            f"Critical Survivors: "
            f"{', '.join(red_locations)}\n"
        )

        f.write(
            f"Stable Survivors: "
            f"{', '.join(yellow_locations)}\n"
        )

    print(f"Results saved to: {results_path}")


if __name__ == "__main__":
    main()

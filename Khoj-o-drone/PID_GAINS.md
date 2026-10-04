# Task 1B — PID Gain Record

## Recorded final throttle gains
- **Kp:** 1000
- **Ki:** 15
- **Kd:** 60

Only the throttle/Z axis was tuned.

## Tuning observations
- Lower Kp settings did not reliably lift/hold the simulated drone at the target.
- At Kp 1000, Ki 0, Kd 5, error reached near target but had large excursions.
- More derivative action reduced the large oscillation.
- With Kp 1000, Ki 10, Kd 60, observed samples were within the ±0.4 band.
- The final recorded setting was Kp 1000, Ki 15, Kd 60.

## Validation criterion
Confirm `throttle_error` enters **[-0.4, +0.4] within 5 seconds** and remains there for **10 seconds**. Revalidate if the environment or controller changes. Pitch and roll are not the tuning targets for this task.

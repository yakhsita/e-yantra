# e-Yantra 2026–27 — Khoj-O-Drone Task 1B

Companion documentation and helper scripts for Task 1B. This is not a replacement for the official e-Yantra source repository.

## Objective
Tune only the Z/throttle PID. The `throttle_error` on `/pos_error` must enter **[-0.4, +0.4] within 5 seconds** and remain there for 10 seconds. Pitch and roll are not the tuning target.

## Recorded throttle gains
| Kp | Ki | Kd |
|---:|---:|---:|
| 1000 | 15 | 60 |

These are the gains from our run, not a guarantee of identical behavior on every setup. Validate settling before capturing evidence.

## Files
- `INSTALLATION.md` — environment and terminal-by-terminal run instructions
- `PID_GAINS.md` — gain record and observed tuning notes
- `run_task_1b.sh` — prints the commands for the three ROS terminals
- `record_task_1b.sh` — records the required topics
- `.gitignore` — excludes generated build/bag outputs

## Recording and submission
Record `/pos_error` and `/whycode_node/markers` for at least 60 seconds. The bag should contain `task_1b_0.db3` and `metadata.yaml`; package these as `KD_<team_id>_task_1b.zip` per the competition instructions. Submit the ZIP and required continuous video through your team's submission process. Keep generated bag data out of this source-code repository unless your team explicitly requests it.

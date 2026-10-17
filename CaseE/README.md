# Case E — results

Project-scale, Rates, Bronx County, 24 hourly build/no-build scenarios
(48 runs total), year 2027. Metric: campaign wall-clock (baselines: sum of the 48 sequential runs;
uTECH-Turbo MOVES: slowest of the 48 concurrent runs).

| Platform | Campaign wall-clock |
|---|---|
| EPA MOVES (Windows) | **99.97 min** |
| EPA MOVES (Linux) | **79.2 min** |
| uTECH-Turbo MOVES | **5.10 min** |

**Speedup:** 19.6x vs. Windows, 15.5x vs. Linux.

## Files in this folder

`measurement/` contains the per-run pipeline logs and output for all three
platforms, plus `compute_results.py`, which recomputes the numbers above
directly from those logs (`python3 measurement/compute_results.py`).

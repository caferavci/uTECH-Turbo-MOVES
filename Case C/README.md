# Case C — results

Default-scale, Inventory, region-wide (8-county) annual RunSpec, year 2025.
Metric: single-run wall-clock.

| Platform | Wall-clock |
|---|---|
| EPA MOVES (Windows) | **91.45 min** |
| EPA MOVES (Linux) | **93.55 min** |
| uTECH-Turbo MOVES | **16.5 min** |

**Speedup:** 5.5x vs. Windows, 5.7x vs. Linux.

## Files in this folder

`measurement/` contains the full pipeline logs and output for all three
platforms, plus `compute_results.py`, which recomputes the numbers above
directly from those logs (`python3 measurement/compute_results.py`).

## Resource profiling

`measurement/Turbo/profiling/` has a dedicated CPU/memory/disk profile of
uTECH-Turbo MOVES's 13-container split architecture on this RunSpec
(`resource_monitor.csv`, sampled every ~3s, same column format as the
Windows leg's monitor), plus `timing.txt`.

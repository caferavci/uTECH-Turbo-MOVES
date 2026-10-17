# Case F — results

Default-scale, Rates, 8 counties x 12 months (96 county-month combinations
total), year 2025. Metric: single-run wall-clock.

The full 96-combination scope could not be executed directly on EPA MOVES
Windows/Linux. A 21-combination subset (3 counties x 7 months) was measured
directly and used to project the full-scope runtime.

| Platform | Measured (21/96 combinations) | Full scope (96/96 combinations) |
|---|---|---|
| EPA MOVES (Windows) | 306.7 min | **1,402.1 min** (projected) |
| EPA MOVES (Linux) | 94.98 min | **434.2 min** (projected) |
| uTECH-Turbo MOVES | — | **18.60 min** (measured directly, max across counties) |

uTECH-Turbo MOVES runs each county as its own independent 13-container
campaign in parallel (one per county, per the architecture used in every
other case in this study); the full-scope campaign time is the max across
all 8 counties' individually-measured times, not a sum. All 8 were measured
directly (17.87–18.60 min each; see `measurement/Turbo/<County>/timing.txt`).

**Speedup (full scope):** 75.4x vs. Windows, 23.3x vs. Linux.

## Files in this folder

`measurement/` contains the pipeline logs and output for all three platforms,
plus `compute_results.py`, which recomputes the numbers above directly from
those logs (`python3 measurement/compute_results.py`).

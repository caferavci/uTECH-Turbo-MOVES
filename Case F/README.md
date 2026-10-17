# Case F — results

Default-scale, Rates, 8 counties x 12 months (96 county-month combinations),
year 2025. Metric: single-run wall-clock.

| Platform | Wall-clock |
|---|---|
| EPA MOVES (Windows) | **906.88 min** |
| EPA MOVES (Linux) | **958.65 min** |
| uTECH-Turbo MOVES | **18.60 min** |

uTECH-Turbo MOVES runs each county as its own independent 13-container
campaign in parallel; the campaign time is the max across the 8 counties
(17.87–18.60 min each; see `measurement/Turbo/<County>/timing.txt`).

**Speedup:** 48.8x vs. Windows, 51.5x vs. Linux.

## Files in this folder

`measurement/` contains the timing files for all three platforms, plus
`compute_results.py`, which recomputes the numbers above directly from them
(`python3 measurement/compute_results.py`). `emissions_summary.tsv` in the
Windows and Linux folders aggregates each run's `rateperdistance` output by
`(pollutantID, processID)`.

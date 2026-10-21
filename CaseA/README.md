# Case A — results

County-scale, Inventory, 8 counties (Bronx, Kings, Nassau, New York, Queens,
Richmond, Suffolk, Westchester), year 2023. Metric: campaign wall-clock
(sum across all 8 counties).

| Platform | Campaign wall-clock |
|---|---|
| EPA MOVES (Windows) | **53.25 min** (55.25 min including import/convert) |
| EPA MOVES (Linux) | **36.57 min** |
| uTECH-Turbo MOVES | **7.02 min** |

**Speedup:** 7.6x vs. Windows, 5.2x vs. Linux.

## Files in this folder

`measurement/` contains the per-county pipeline logs and output for all three
platforms, plus `compute_results.py`, which recomputes the numbers above
directly from those logs (`python3 measurement/compute_results.py`).

## Output equivalence

Each platform's `measurement/<Platform>/<County>/` folder has an
`emissions_summary.txt`/`.tsv` file: the `movesoutput` rows grouped by
`(pollutantID, processID)`, with summed `emissionQuant` and row count.
`measurement/compare_outputs.py` reads all three platforms' summaries for
all 8 counties and reports row counts, max absolute difference, max
relative difference, and whether the results are bit-identical
(`python3 measurement/compare_outputs.py`).

Result, across all 8 counties: **row counts match exactly** in every
`(pollutantID, processID)` group; emission totals agree to ~8-9 significant
figures (max relative difference **2.13e-09**), taken across all three platforms.

The full Linux output database for New York County is included at
`measurement/Linux/NewYork/runspec_outputdb.zip`.

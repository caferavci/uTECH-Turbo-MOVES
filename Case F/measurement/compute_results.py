#!/usr/bin/env python3
"""Recompute Case F's headline numbers directly from the raw logs in this folder.

Windows and Linux measured 21 of the 96 county-month combinations directly;
the 96-cell figures are a linear extrapolation from that 21-cell measurement
(see ../README.md). Turbo runs each county as its own independent
13-container campaign in parallel; its full-scope number is the max across
all 8 counties' directly-measured campaign times (measurement/Turbo/<County>/timing.txt),
not a sum or an extrapolation.

Run from anywhere: python3 compute_results.py
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
MEASURED_CELLS = 21
FULL_CELLS = 96
COUNTIES = ["Bronx", "Kings", "Nassau", "NewYork", "Queens", "Richmond", "Suffolk", "Westchester"]


def read_text(path):
    for enc in ("utf-16", "utf-8"):
        try:
            with open(path, encoding=enc) as f:
                return f.read()
        except UnicodeError:
            continue
    with open(path, encoding="latin-1") as f:
        return f.read()


def total_time_sec(path):
    text = read_text(path)
    m = re.search(r"Total time:\s*(?:(\d+)\s*minutes?)?\s*(\d+)\s*seconds?", text)
    if not m:
        return None
    mins = int(m.group(1)) if m.group(1) else 0
    return mins * 60 + int(m.group(2))


def wrapper_elapsed_sec(path):
    m = re.search(r"wrapper_elapsed_sec=(\d+)", read_text(path))
    return int(m.group(1)) if m else None


def turbo_campaign_max_sec(path):
    text = read_text(path)
    m = re.search(r"campaign_max_sec=(\d+)", text)
    return int(m.group(1)) if m else None


def main():
    win_sec = total_time_sec(os.path.join(HERE, "Windows", "CaseF_21cell_cloud_io2_run.log"))
    lin_sec = wrapper_elapsed_sec(os.path.join(HERE, "Linux", "wrapper_timing.txt"))

    turbo_max_sec = 0
    for c in COUNTIES:
        sec = turbo_campaign_max_sec(os.path.join(HERE, "Turbo", c, "timing.txt"))
        turbo_max_sec = max(turbo_max_sec, sec)
    turbo_min = turbo_max_sec / 60

    win_min = win_sec / 60
    lin_min = lin_sec / 60
    win_full_min = win_min / MEASURED_CELLS * FULL_CELLS
    lin_full_min = lin_min / MEASURED_CELLS * FULL_CELLS

    print(f"Case F -- recomputed from raw logs in this folder ({MEASURED_CELLS}/{FULL_CELLS} cells measured)")
    print(f"{'Platform':<22}{'Measured':>12}   {'Full scope':>14}   README")
    print(f"{'EPA MOVES (Windows)':<22}{win_min:>9.2f} min   {win_full_min:>11.1f} min   306.7 -> 1402.1 min")
    print(f"{'EPA MOVES (Linux)':<22}{lin_min:>9.2f} min   {lin_full_min:>11.1f} min   94.98 -> 434.2 min")
    print(f"{'uTECH-Turbo MOVES':<22}{'--':>9}       {turbo_min:>11.2f} min   18.60 min (measured directly, max across 8 counties)")
    print()
    print(f"Speedup vs Windows (full scope): {win_full_min/turbo_min:.1f}x")
    print(f"Speedup vs Linux (full scope):   {lin_full_min/turbo_min:.1f}x")


if __name__ == "__main__":
    main()

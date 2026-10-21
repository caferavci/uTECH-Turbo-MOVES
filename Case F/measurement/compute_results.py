#!/usr/bin/env python3
"""Recompute Case F's headline numbers from the timing files in this folder.

Run from anywhere: python3 compute_results.py
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
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


def first_float(path, pattern):
    return float(re.search(pattern, read_text(path)).group(1))


def main():
    win_min = first_float(os.path.join(HERE, "Windows", "CaseF_96cell_result.txt"), r"elapsed_seconds=([\d.]+)") / 60
    lin_min = first_float(os.path.join(HERE, "Linux", "wrapper_timing.txt"), r"wrapper_elapsed_sec=(\d+)") / 60
    turbo_min = max(
        first_float(os.path.join(HERE, "Turbo", c, "timing.txt"), r"campaign_max_sec=(\d+)") for c in COUNTIES
    ) / 60

    print("Case F -- full scope (96 county-month combinations)")
    print(f"{'EPA MOVES (Windows)':<22}{win_min:>9.2f} min")
    print(f"{'EPA MOVES (Linux)':<22}{lin_min:>9.2f} min")
    print(f"{'uTECH-Turbo MOVES':<22}{turbo_min:>9.2f} min   (max across 8 counties)")
    print()
    print(f"Speedup vs Windows: {win_min/turbo_min:.1f}x")
    print(f"Speedup vs Linux:   {lin_min/turbo_min:.1f}x")


if __name__ == "__main__":
    main()

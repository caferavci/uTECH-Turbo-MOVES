#!/usr/bin/env python3
"""Recompute Case C's headline numbers directly from the raw logs in this folder.

Run from anywhere: python3 compute_results.py
"""
import csv
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))


def read_text(path):
    for enc in ("utf-16", "utf-8"):
        try:
            with open(path, encoding=enc) as f:
                return f.read()
        except UnicodeError:
            continue
    with open(path, encoding="latin-1") as f:
        return f.read()


def windows_elapsed_sec(path):
    """Wall-clock seconds recorded by the timing wrapper (RESULT line)."""
    m = re.search(r"elapsed_seconds=([\d.]+)", read_text(path))
    return float(m.group(1))


def wrapper_elapsed_sec(path):
    m = re.search(r"wrapper_elapsed_sec=(\d+)", read_text(path))
    return int(m.group(1))


def main():
    win_sec = windows_elapsed_sec(os.path.join(HERE, "Windows", "campaign_wrapper.log"))
    lin_sec = wrapper_elapsed_sec(os.path.join(HERE, "Linux", "wrapper_timing.txt"))

    with open(os.path.join(HERE, "Turbo", "CaseC_metrics_summary.csv")) as f:
        row = next(csv.DictReader(f))
    turbo_min = float(row["wall_clock_min"])

    print("Case C -- recomputed from raw logs in this folder")
    print(f"{'Platform':<22}{'Computed':>12}   README")
    print(f"{'EPA MOVES (Windows)':<22}{win_sec/60:>9.2f} min   91.45 min")
    print(f"{'EPA MOVES (Linux)':<22}{lin_sec/60:>9.2f} min   93.55 min")
    print(f"{'uTECH-Turbo MOVES':<22}{turbo_min:>9.2f} min   16.5 min")
    print()
    print(f"Speedup vs Windows: {win_sec/60/turbo_min:.1f}x")
    print(f"Speedup vs Linux:   {lin_sec/60/turbo_min:.1f}x")


if __name__ == "__main__":
    main()

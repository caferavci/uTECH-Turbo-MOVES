#!/usr/bin/env python3
"""Recompute Case E's headline numbers directly from the raw logs in this folder.

Run from anywhere: python3 compute_results.py
"""
import glob
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


def main():
    campaign_txt = read_text(os.path.join(HERE, "Windows", "campaign_results.txt"))
    win_sec = sum(float(m) for m in re.findall(r"elapsed_seconds=([\d.]+)", campaign_txt))
    win_runs = len(re.findall(r"elapsed_seconds=", campaign_txt))

    lin_sec = 0
    lin_runs = 0
    for d in sorted(glob.glob(os.path.join(HERE, "Linux", "*"))):
        timing_path = os.path.join(d, "wrapper_timing.txt")
        if os.path.exists(timing_path):
            m = re.search(r"wrapper_elapsed_sec=(\d+)", read_text(timing_path))
            if m:
                lin_sec += int(m.group(1))
                lin_runs += 1

    turbo_max_min = 0.0
    turbo_runs = 0
    for d in sorted(glob.glob(os.path.join(HERE, "Turbo", "*"))):
        metrics_path = os.path.join(d, "metrics.txt")
        if os.path.exists(metrics_path):
            m = re.search(r"Wall-clock time:\s+([\d.]+)\s+min", read_text(metrics_path))
            if m:
                turbo_max_min = max(turbo_max_min, float(m.group(1)))
                turbo_runs += 1

    print("Case E -- recomputed from raw logs in this folder (48-run campaign)")
    print(f"{'Platform':<22}{'Computed':>12}   README")
    print(f"{'EPA MOVES (Windows)':<22}{win_sec/60:>9.2f} min   99.97 min  ({win_runs} runs)")
    print(f"{'EPA MOVES (Linux)':<22}{lin_sec/60:>9.2f} min   79.2 min  ({lin_runs} runs)")
    print(f"{'uTECH-Turbo MOVES':<22}{turbo_max_min:>9.2f} min   5.10 min  ({turbo_runs} runs, max wall-clock)")
    print()
    print(f"Speedup vs Windows: {win_sec/60/turbo_max_min:.1f}x")
    print(f"Speedup vs Linux:   {lin_sec/60/turbo_max_min:.1f}x")


if __name__ == "__main__":
    main()

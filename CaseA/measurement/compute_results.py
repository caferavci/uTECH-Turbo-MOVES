#!/usr/bin/env python3
"""Recompute Case A's headline numbers directly from the raw logs in this folder.

Run from anywhere: python3 compute_results.py
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
COUNTIES = ["Bronx", "Kings", "Nassau", "NewYork", "Queens", "Richmond", "Suffolk", "Westchester"]
TURBO_WARMUP_OFFSET_SEC = 345  # see ../README.md


def read_text(path):
    for enc in ("utf-16", "utf-8"):
        try:
            with open(path, encoding=enc) as f:
                return f.read()
        except UnicodeError:
            continue
    with open(path, encoding="latin-1") as f:
        return f.read()


def wrapper_elapsed_sec(path):
    text = read_text(path)
    m = re.search(r"wrapper_elapsed_sec=(\d+)", text)
    return int(m.group(1)) if m else None


def windows_campaign(path):
    """Per-county wall-clock seconds and campaign total from campaign_results.txt."""
    text = read_text(path)
    per_county = {c: float(s) for c, s in re.findall(r"RESULT \[(\w+)\]: elapsed_seconds=([\d.]+)", text)}
    total = float(re.search(r"CAMPAIGN_TOTAL_SECONDS=([\d.]+)", text).group(1))
    return per_county, total


def turbo_campaign_max_sec(path):
    text = read_text(path)
    m = re.search(r"campaign_max_sec=(\d+)", text)
    return int(m.group(1)) if m else None


def main():
    win_per_county, win_full_total = windows_campaign(os.path.join(HERE, "Windows", "campaign_results.txt"))
    win_run_total = 0
    lin_total = 0
    turbo_max_raw = 0

    for c in COUNTIES:
        win_run_total += win_per_county[c]

        lin_sec = wrapper_elapsed_sec(os.path.join(HERE, "Linux", c, "wrapper_timing.txt"))
        lin_total += lin_sec

        turbo_sec = turbo_campaign_max_sec(os.path.join(HERE, "Turbo", c, "timing.txt"))
        turbo_max_raw = max(turbo_max_raw, turbo_sec)

    turbo_campaign_min = (turbo_max_raw + TURBO_WARMUP_OFFSET_SEC) / 60

    print("Case A -- recomputed from raw logs in this folder")
    print(f"{'Platform':<22}{'Computed':>12}   README")
    print(f"{'EPA MOVES (Windows)':<22}{win_run_total/60:>9.2f} min   53.25 min (run-only)")
    print(f"{'  + import/convert':<22}{win_full_total/60:>9.2f} min   55.25 min")
    print(f"{'EPA MOVES (Linux)':<22}{lin_total/60:>9.2f} min   36.57 min")
    print(f"{'uTECH-Turbo MOVES':<22}{turbo_campaign_min:>9.2f} min   7.02 min")
    print()
    print(f"Speedup vs Windows: {win_run_total/60/turbo_campaign_min:.1f}x")
    print(f"Speedup vs Linux:   {lin_total/60/turbo_campaign_min:.1f}x")


if __name__ == "__main__":
    main()

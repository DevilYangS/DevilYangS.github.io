#!/usr/bin/env python
"""Refresh aggregate Google Scholar metrics (citations / h-index / i10-index)
into _data/scholar_metrics.yml, which the homepage reads via Liquid.

Uses plain HTTP + regex so it works without extra dependencies beyond
requests/pyyaml (both already in requirements.txt).
"""

import os
import re
import sys
from datetime import datetime, timezone, timedelta

import requests
import yaml

CONFIG_FILE = "_data/socials.yml"
OUTPUT_FILE = "_data/scholar_metrics.yml"
HOSTS = [
    "https://scholar.google.com",
    "https://scholar.google.com.hk",
]
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


def load_user_id() -> str:
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}
    uid = cfg.get("scholar_userid")
    if not uid:
        print("scholar_userid missing in _data/socials.yml")
        sys.exit(1)
    return uid


def fetch_profile_html(uid: str) -> str:
    errors = []
    for host in HOSTS:
        url = f"{host}/citations?hl=en&user={uid}"
        try:
            r = requests.get(url, headers=HEADERS, timeout=40)
            if r.status_code == 200 and "gsc_rsb_std" in r.text:
                return r.text
            errors.append(f"{host}: HTTP {r.status_code}")
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{host}: {exc}")
    raise RuntimeError("; ".join(errors) or "no host attempted")


def parse_metrics(html: str) -> dict:
    vals = re.findall(r'<td class="gsc_rsb_std">([\d,]+)</td>', html)
    if len(vals) < 6:
        raise RuntimeError(f"unexpected profile page (found {len(vals)} metric cells)")
    v = [int(x.replace(",", "")) for x in vals[:6]]
    return {
        "citations": v[0],
        "citations_since": v[1],
        "h_index": v[2],
        "h_index_since": v[3],
        "i10_index": v[4],
        "i10_index_since": v[5],
    }


def main() -> None:
    uid = load_user_id()
    html = fetch_profile_html(uid)
    metrics = parse_metrics(html)
    tz = timezone(timedelta(hours=8))
    metrics["last_updated"] = datetime.now(tz).strftime("%b. %d, %Y").replace(". 0", ". ")
    metrics["scholar_id"] = uid

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        yaml.safe_dump(metrics, f, allow_unicode=True, sort_keys=False)
    print(f"updated {OUTPUT_FILE}: {metrics}")


if __name__ == "__main__":
    main()

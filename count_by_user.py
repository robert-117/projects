#!/usr/bin/python3

import argparse, json, sys
from collections import Counter

def parse_args():
    p = argparse.ArgumentParser(description="Count log entries per user_id from the JSONL file")
    p.add_argument("file", help="path to .jsonl log file")
    return p.parse_args()

def main():
    args = parse_args()
    counts = Counter()

    try:
        with open(args.file, "r", encoding="utf-8") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"[WARN] line {lineno}: invalid JSON ({e})", file=sys.stderr)
                    continue

                user = rec.get("user_id")
                if not user:
                    print(f"[WARN] line {lineno}: missing user_id", file=sys.stderr)
                    continue

                counts[user] += 1
    except FileNotFoundError:
        print(f"[ERR] file not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    # print results, sorted by count desc then user_id asc
    for user, cnt in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"{user},{cnt}")

if __name__ == "__main__":
    main()
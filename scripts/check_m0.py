#!/usr/bin/env python3
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

required = [
    "README.md",
    "ROADMAP.md",
    "LICENSE",
    "docs/ARCHITECTURE.md",
    "targets/targets.json",
    "include/amistudio/backend.h",
    "src/backend.c",
]

for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f"missing required file: {rel}")

try:
    data = json.loads((ROOT / "targets/targets.json").read_text())
except Exception as exc:
    errors.append(f"cannot parse targets/targets.json: {exc}")
    data = {}

if data.get("format_version") != 1:
    errors.append("target format_version must be 1")

expected = {
    "amiga-a500-ocs",
    "amiga-a500plus-ecs",
    "amiga-a600-ecs",
    "amiga-a1200-aga",
    "amiga-cd32-aga",
}
seen = {item.get("id") for item in data.get("targets", []) if isinstance(item, dict)}
missing = expected - seen
if missing:
    errors.append("missing baseline target(s): " + ", ".join(sorted(missing)))

for item in data.get("targets", []):
    if not isinstance(item, dict):
        errors.append("target entry must be an object")
        continue
    for key in ("id", "cpu", "chipset", "chip_ram_kib", "fast_ram_kib"):
        if key not in item:
            errors.append(f"target {item.get('id','<unknown>')} missing {key}")

arch = (ROOT / "docs/ARCHITECTURE.md").read_text() if (ROOT / "docs/ARCHITECTURE.md").exists() else ""
if "RetroStudio must never depend on AmiStudio" not in arch:
    errors.append("dependency rule is missing")

header = (ROOT / "include/amistudio/backend.h").read_text() if (ROOT / "include/amistudio/backend.h").exists() else ""
if "AMISTUDIO_RETROSTUDIO_TARGET_API_VERSION 1u" not in header:
    errors.append("RetroStudio target API version marker is missing")

if errors:
    print("M0 CHECK: FAIL")
    for error in errors:
        print(f"  FAIL: {error}")
    sys.exit(1)

print("M0 CHECK: PASS")
print("  PASS: repository foundation present")
print("  PASS: baseline Amiga target profiles present")
print("  PASS: target profile JSON parses")
print("  PASS: backend API boundary versioned")
print("  PASS: RetroStudio dependency direction documented")

"""Loading utilities for vault data from files."""

import json
import csv
import os

from storage.serializer import vault_from_dict, rune_from_dict
from vault import Vault


def load_json(filepath):
    """Load a vault from a JSON file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    with open(filepath) as f:
        data = json.load(f)
    return vault_from_dict(data)


def load_csv(filepath):
    """Load a vault from a CSV file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    vault = Vault()
    with open(filepath) as f:
        reader = csv.DictReader(f)
        for row in reader:
            rune_data = {
                "id": int(row.get("id", 0)),
                "name": row.get("name", ""),
                "stage": row.get("stage", "blank"),
            }
            rune = rune_from_dict(rune_data)
            vault._runes.add(rune)
            if rune.id > vault._counter:
                vault._counter = rune.id
    return vault


def detect_format(filepath):
    """Detect the file format based on extension."""
    _, ext = os.path.splitext(filepath)
    format_map = {
        ".json": "json",
        ".csv": "csv",
        ".txt": "text",
    }
    return format_map.get(ext.lower(), "unknown")


def load_auto(filepath):
    """Auto-detect format and load a vault."""
    fmt = detect_format(filepath)
    if fmt == "json":
        return load_json(filepath)
    if fmt == "csv":
        return load_csv(filepath)
    raise ValueError(f"Cannot auto-load format: {fmt}")

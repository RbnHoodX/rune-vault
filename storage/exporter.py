"""Export utilities for vault data."""

import csv
import json
import io

from storage.serializer import vault_to_dict, rune_to_dict
from config import SUPPORTED_EXPORT_FORMATS


def export_text(vault, stream=None):
    """Export vault as human-readable text."""
    close = False
    if stream is None:
        stream = io.StringIO()
        close = True

    runes = vault.runes()
    stream.write(f"Rune Vault ({len(runes)} runes)\n")
    stream.write("=" * 40 + "\n")

    for rune in runes:
        stream.write(f"  [{rune.id}] {rune.name} ({rune.stage})\n")

    if close:
        return stream.getvalue()


def export_csv(vault, filepath):
    """Export vault as CSV."""
    runes = vault.runes()
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "stage"])
        writer.writeheader()
        for rune in runes:
            writer.writerow(rune_to_dict(rune))


def export_json(vault, filepath):
    """Export vault as JSON."""
    data = vault_to_dict(vault)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)


def summary(vault):
    """Generate a summary of the vault contents."""
    runes = vault.runes()
    stages = {}
    for r in runes:
        stages[r.stage] = stages.get(r.stage, 0) + 1

    return {
        "total": len(runes),
        "stages": stages,
        "has_runes": len(runes) > 0,
    }


def validate_format(fmt):
    """Validate an export format string."""
    if fmt not in SUPPORTED_EXPORT_FORMATS:
        raise ValueError(
            f"Unsupported format: {fmt!r}. "
            f"Choose from: {', '.join(SUPPORTED_EXPORT_FORMATS)}"
        )
    return fmt

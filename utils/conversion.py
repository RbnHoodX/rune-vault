"""Data conversion utilities for rune vault."""


def rune_to_text(rune):
    """Convert a rune to a text line."""
    return f"{rune.id}\t{rune.name}\t{rune.stage}"


def text_to_fields(line):
    """Parse a tab-separated text line into field dict."""
    parts = line.strip().split("\t")
    if len(parts) < 3:
        return None
    return {
        "id": int(parts[0]),
        "name": parts[1],
        "stage": parts[2],
    }


def vault_to_text_lines(vault):
    """Convert all runes in a vault to text lines."""
    lines = []
    for rune in sorted(vault.runes(), key=lambda r: r.id):
        lines.append(rune_to_text(rune))
    return lines


def batch_names(vault):
    """Extract all rune names as a sorted list."""
    return sorted({r.name for r in vault.runes()})


def batch_stages(vault):
    """Extract all unique stages present in the vault."""
    return sorted({r.stage for r in vault.runes()})


def rune_to_csv_row(rune, delimiter=","):
    """Convert a rune to a CSV-style row string."""
    return delimiter.join([str(rune.id), rune.name, rune.stage])


def csv_header(delimiter=","):
    """Return the CSV header for rune data."""
    return delimiter.join(["id", "name", "stage"])


def runes_to_lookup(vault):
    """Build a name -> list of runes lookup dictionary."""
    lookup = {}
    for r in vault.runes():
        lookup.setdefault(r.name, []).append(r)
    return lookup


def runes_to_id_map(vault):
    """Build an id -> rune lookup dictionary."""
    return {r.id: r for r in vault.runes()}


def merge_names(names_a, names_b):
    """Merge two name lists, deduplicating and sorting."""
    combined = set(names_a) | set(names_b)
    return sorted(combined)


def stage_progression(current, target, valid_stages=None):
    """Check if target stage comes after current in progression."""
    if valid_stages is None:
        from config import RUNE_STAGES
        valid_stages = RUNE_STAGES
    if current not in valid_stages or target not in valid_stages:
        return False
    return valid_stages.index(target) > valid_stages.index(current)

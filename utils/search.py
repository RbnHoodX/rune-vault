"""Search and filter utilities for the rune vault."""


def find_by_name(vault, pattern):
    """Find runes whose name contains the pattern (case-insensitive)."""
    pattern_lower = pattern.lower()
    return [r for r in vault.runes() if pattern_lower in r.name.lower()]


def find_exact(vault, name):
    """Find runes with an exact name match."""
    return [r for r in vault.runes() if r.name == name]


def find_by_stage(vault, stage):
    """Find all runes at a given stage."""
    return [r for r in vault.runes() if r.stage == stage]


def find_blank(vault):
    """Find all runes still in blank stage."""
    return find_by_stage(vault, "blank")


def find_by_id(vault, rune_id):
    """Find a rune by its ID, or None."""
    for r in vault.runes():
        if r.id == rune_id:
            return r
    return None


def count_by_stage(vault):
    """Count runes grouped by stage."""
    counts = {}
    for r in vault.runes():
        counts[r.stage] = counts.get(r.stage, 0) + 1
    return counts


def find_duplicates(vault):
    """Find runes with duplicate names."""
    seen = {}
    duplicates = []
    for r in vault.runes():
        if r.name in seen:
            if seen[r.name] not in duplicates:
                duplicates.append(seen[r.name])
            duplicates.append(r)
        else:
            seen[r.name] = r
    return duplicates


def search_names(vault, prefix=None, suffix=None, contains=None):
    """Search runes by name components."""
    results = vault.runes()

    if prefix is not None:
        prefix_lower = prefix.lower()
        results = [r for r in results if r.name.lower().startswith(prefix_lower)]

    if suffix is not None:
        suffix_lower = suffix.lower()
        results = [r for r in results if r.name.lower().endswith(suffix_lower)]

    if contains is not None:
        contains_lower = contains.lower()
        results = [r for r in results if contains_lower in r.name.lower()]

    return results

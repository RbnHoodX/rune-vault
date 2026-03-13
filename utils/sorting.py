"""Sorting utilities for rune collections."""


def sort_by_name(runes, reverse=False):
    """Sort runes alphabetically by name, case-insensitive."""
    return sorted(runes, key=lambda r: r.name.lower(), reverse=reverse)


def sort_by_id(runes, reverse=False):
    """Sort runes by ID."""
    return sorted(runes, key=lambda r: r.id, reverse=reverse)


def sort_by_stage(runes, stage_order=None):
    """Sort runes by stage progression order."""
    if stage_order is None:
        from config import RUNE_STAGES
        stage_order = RUNE_STAGES
    order_map = {s: i for i, s in enumerate(stage_order)}
    return sorted(runes, key=lambda r: order_map.get(r.stage, 999))


def group_by_stage(runes):
    """Group runes by their stage."""
    groups = {}
    for r in runes:
        groups.setdefault(r.stage, []).append(r)
    return groups


def group_by_name(runes):
    """Group runes by their name."""
    groups = {}
    for r in runes:
        groups.setdefault(r.name, []).append(r)
    return groups


def top_n(runes, n, key_func):
    """Return the top N runes by a given key function."""
    return sorted(runes, key=key_func, reverse=True)[:n]


def partition(runes, predicate):
    """Split runes into two lists based on a predicate."""
    yes = []
    no = []
    for r in runes:
        if predicate(r):
            yes.append(r)
        else:
            no.append(r)
    return yes, no

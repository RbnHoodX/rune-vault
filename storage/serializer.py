"""Serialization utilities for runes and vaults."""

from rune import Rune
from vault import Vault


def rune_to_dict(rune):
    """Convert a rune to a dictionary."""
    return {
        "id": rune.id,
        "name": rune.name,
        "stage": rune.stage,
    }


def vault_to_dict(vault):
    """Convert a vault to a dictionary."""
    return {
        "runes": [rune_to_dict(r) for r in vault.runes()],
    }


def rune_from_dict(data):
    """Reconstruct a rune from a dictionary."""
    rune = Rune(name=data.get("name", ""))
    rune.id = data.get("id", 0)
    rune.stage = data.get("stage", "blank")
    return rune


def vault_from_dict(data):
    """Reconstruct a vault from a dictionary."""
    vault = Vault()
    runes_data = data.get("runes", [])
    for rd in runes_data:
        rune = rune_from_dict(rd)
        vault._runes.add(rune)
        if rune.id > vault._counter:
            vault._counter = rune.id
    return vault


def merge_vaults(vault_a, vault_b):
    """Merge two vaults into a new vault. IDs are reassigned."""
    merged = Vault()
    for rune in vault_a.runes():
        new_rune = Rune(name=rune.name)
        new_rune.stage = rune.stage
        merged.inscribe(new_rune)
    for rune in vault_b.runes():
        new_rune = Rune(name=rune.name)
        new_rune.stage = rune.stage
        merged.inscribe(new_rune)
    return merged

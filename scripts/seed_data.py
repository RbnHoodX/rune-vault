"""Seed the vault with example rune data."""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rune import Rune
from vault import Vault


SAMPLE_RUNES = [
    "fehu",
    "uruz",
    "thurisaz",
    "ansuz",
    "raidho",
    "kenaz",
    "gebo",
    "wunjo",
    "hagalaz",
    "nauthiz",
    "isa",
    "jera",
    "algiz",
    "sowilo",
    "tiwaz",
    "berkano",
    "mannaz",
    "laguz",
    "dagaz",
    "othala",
]


def create_sample_vault():
    """Create a vault populated with sample runes."""
    vault = Vault()
    for name in SAMPLE_RUNES:
        rune = Rune(name=name)
        vault.inscribe(rune)
    return vault


def main():
    """Create and display a sample vault."""
    vault = create_sample_vault()
    print(f"Created vault with {len(vault.runes())} runes:")
    for rune in sorted(vault.runes(), key=lambda r: r.id):
        print(f"  {rune}")


if __name__ == "__main__":
    main()

"""Inscription parsing and validation utilities."""

import re

VALID_SCRIPTS = ("futhark", "ogham", "latin", "mixed")

FUTHARK_CHARS = set("ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚾᛁᛃᛇᛈᛉᛊᛏᛒᛖᛗᛚᛜᛞᛟ")
OGHAM_CHARS = set("ᚁᚂᚃᚄᚅᚆᚇᚈᚉᚊᚋᚌᚍᚎᚏᚐᚑᚒᚓᚔ")


def detect_script(text):
    """Detect the script type of an inscription."""
    if not text or not text.strip():
        return "unknown"

    has_futhark = bool(set(text) & FUTHARK_CHARS)
    has_ogham = bool(set(text) & OGHAM_CHARS)
    has_latin = bool(re.search(r"[a-zA-Z]", text))

    if has_futhark and has_ogham:
        return "mixed"
    if has_futhark:
        return "futhark"
    if has_ogham:
        return "ogham"
    if has_latin:
        return "latin"
    return "unknown"


def validate_inscription(text):
    """Validate an inscription string."""
    if not isinstance(text, str):
        raise ValueError("Inscription must be a string")
    stripped = text.strip()
    if not stripped:
        raise ValueError("Inscription cannot be empty")
    if len(stripped) > 500:
        raise ValueError("Inscription too long (max 500 characters)")
    return stripped


def normalize_inscription(text):
    """Normalize whitespace and formatting in an inscription."""
    if not isinstance(text, str):
        return ""
    return " ".join(text.split())


def word_count(text):
    """Count words in an inscription."""
    if not isinstance(text, str) or not text.strip():
        return 0
    return len(text.split())


def char_frequency(text):
    """Get character frequency distribution of an inscription."""
    freq = {}
    for ch in text:
        if ch.strip():
            freq[ch] = freq.get(ch, 0) + 1
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))


def contains_rune_chars(text):
    """Check if text contains any Unicode rune characters."""
    return bool(set(text) & (FUTHARK_CHARS | OGHAM_CHARS))


def split_inscription(text, delimiter="|"):
    """Split a compound inscription into parts."""
    if not isinstance(text, str):
        return []
    return [part.strip() for part in text.split(delimiter) if part.strip()]

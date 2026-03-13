"""Display formatting utilities for rune vault output."""

from config import RUNE_STAGES


def format_rune(rune, show_id=True):
    """Format a single rune for display."""
    parts = []
    if show_id:
        parts.append(f"[{rune.id}]")
    parts.append(rune.name or "(unnamed)")
    parts.append(f"({rune.stage})")
    return " ".join(parts)


def format_rune_detail(rune):
    """Format a rune with all available attributes."""
    lines = [
        f"Rune #{rune.id}",
        f"  Name:  {rune.name}",
        f"  Stage: {rune.stage}",
    ]
    return "\n".join(lines)


def format_table(runes, columns=None, show_ids=True):
    """Format runes as a text table."""
    if not runes:
        return "(empty)"

    if columns is None:
        columns = ["id", "name", "stage"]

    if not show_ids and "id" in columns:
        columns = [c for c in columns if c != "id"]

    header = " | ".join(col.upper().ljust(20) for col in columns)
    separator = "-+-".join("-" * 20 for _ in columns)

    rows = []
    for rune in runes:
        cells = []
        for col in columns:
            value = getattr(rune, col, "")
            cells.append(str(value).ljust(20))
        rows.append(" | ".join(cells))

    return "\n".join([header, separator] + rows)


def format_stage_progression(current_stage):
    """Show the progression of stages with current highlighted."""
    parts = []
    for stage in RUNE_STAGES:
        if stage == current_stage:
            parts.append(f"[{stage}]")
        else:
            parts.append(stage)
    return " -> ".join(parts)


def truncate(text, max_length=40):
    """Truncate text with ellipsis if too long."""
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."


def indent_lines(text, level=1, width=2):
    """Indent each line of text."""
    prefix = " " * (level * width)
    return "\n".join(prefix + line for line in text.split("\n"))


def format_count(count, singular, plural=None):
    """Format a count with proper singular/plural form."""
    if plural is None:
        plural = singular + "s"
    word = singular if count == 1 else plural
    return f"{count} {word}"


def format_percentage(part, total):
    """Format a value as a percentage of total."""
    if total == 0:
        return "0.0%"
    pct = (part / total) * 100
    return f"{pct:.1f}%"

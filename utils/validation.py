"""Input validation utilities for the rune vault system."""

from config import RUNE_STAGES, MAX_VAULT_SIZE


def validate_name(name):
    """Validate a rune name. Returns cleaned name or raises ValueError."""
    if not isinstance(name, str):
        raise ValueError("Name must be a string")
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("Name cannot be blank")
    if len(cleaned) > 200:
        raise ValueError("Name too long (max 200 characters)")
    return cleaned


def validate_stage(stage):
    """Validate that a stage is recognized."""
    if stage not in RUNE_STAGES:
        raise ValueError(f"Unknown stage: {stage!r}")
    return stage


def validate_id(rune_id):
    """Validate a rune ID."""
    if not isinstance(rune_id, int):
        raise ValueError("ID must be an integer")
    if rune_id < 0:
        raise ValueError("ID must be non-negative")
    return rune_id


def validate_vault_capacity(current_size):
    """Check if the vault can accept more runes."""
    if current_size >= MAX_VAULT_SIZE:
        raise ValueError(f"Vault at maximum capacity ({MAX_VAULT_SIZE})")
    return True


def is_valid_name(name):
    """Check if a name is valid without raising."""
    try:
        validate_name(name)
        return True
    except (ValueError, TypeError):
        return False


def is_valid_stage(stage):
    """Check if a stage is valid without raising."""
    return stage in RUNE_STAGES


def sanitize_text(text):
    """Clean and sanitize text input."""
    if not isinstance(text, str):
        return ""
    return " ".join(text.split())


def validate_positive_int(value, field_name="value"):
    """Validate that a value is a positive integer."""
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError(f"{field_name} must be an integer")
    if value < 1:
        raise ValueError(f"{field_name} must be positive")
    return value


def validate_range(value, low, high, field_name="value"):
    """Validate that a value is within a range."""
    if not isinstance(value, (int, float)):
        raise ValueError(f"{field_name} must be numeric")
    if value < low or value > high:
        raise ValueError(f"{field_name} must be between {low} and {high}")
    return value

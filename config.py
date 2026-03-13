"""Configuration settings for the rune vault system."""

VERSION = "0.1.0"
APP_NAME = "rune-vault"

MAX_VAULT_SIZE = 10000
DEFAULT_RUNE_NAME = "unnamed"

SUPPORTED_EXPORT_FORMATS = ("text", "csv", "json")
DATA_DIR = "data"
LOG_LEVEL = "INFO"

RUNE_STAGES = (
    "blank",
    "drafted",
    "carved",
    "enchanted",
    "sealed",
    "archived",
)

POWER_THRESHOLDS = {
    "dormant": (0, 2),
    "faint": (3, 5),
    "strong": (6, 8),
    "mythic": (9, 10),
}


class Settings:
    """Runtime configuration container."""

    _defaults = {
        "max_vault_size": MAX_VAULT_SIZE,
        "default_name": DEFAULT_RUNE_NAME,
        "export_format": "text",
        "log_level": LOG_LEVEL,
        "auto_save": False,
        "strict_mode": True,
    }

    def __init__(self, **kwargs):
        for key, default in self._defaults.items():
            setattr(self, key, kwargs.get(key, default))
        unknown = set(kwargs) - set(self._defaults)
        if unknown:
            raise ValueError(f"Unknown settings: {unknown}")

    def as_dict(self):
        return {key: getattr(self, key) for key in self._defaults}

    @classmethod
    def from_dict(cls, data):
        return cls(**{k: v for k, v in data.items() if k in cls._defaults})

    def __repr__(self):
        pairs = ", ".join(f"{k}={v!r}" for k, v in self.as_dict().items())
        return f"Settings({pairs})"

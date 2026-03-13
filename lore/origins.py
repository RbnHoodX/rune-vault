"""Rune origin and provenance classification."""

RUNE_ORIGINS = {
    "elder_futhark": {
        "name": "Elder Futhark",
        "era": "ancient",
        "region": "Scandinavia",
        "runes": [
            "fehu", "uruz", "thurisaz", "ansuz", "raidho", "kenaz",
            "gebo", "wunjo", "hagalaz", "nauthiz", "isa", "jera",
            "eihwaz", "perthro", "algiz", "sowilo", "tiwaz", "berkano",
            "ehwaz", "mannaz", "laguz", "ingwaz", "dagaz", "othala",
        ],
    },
    "younger_futhark": {
        "name": "Younger Futhark",
        "era": "medieval",
        "region": "Scandinavia",
        "runes": [
            "fe", "ur", "thurs", "ass", "reith", "kaun",
            "hagall", "nauth", "iss", "ar", "sol", "tyr",
            "bjarkan", "mathr", "logr", "yr",
        ],
    },
    "anglo_saxon": {
        "name": "Anglo-Saxon Futhorc",
        "era": "medieval",
        "region": "Britain",
        "runes": [
            "feoh", "ur", "thorn", "os", "rad", "cen",
            "gyfu", "wen", "haegl", "nyd", "is", "ger",
            "eoh", "peorth", "eolh", "sigel", "tir", "beorc",
            "eh", "mann", "lagu", "ing", "daeg", "ethel",
            "ac", "aesc", "yr", "ior", "ear",
        ],
    },
    "ogham": {
        "name": "Ogham",
        "era": "ancient",
        "region": "Ireland",
        "runes": [
            "beith", "luis", "fearn", "saille", "nion",
            "huath", "duir", "tinne", "coll", "quert",
            "muin", "gort", "ngetal", "straif", "ruis",
            "ailm", "onn", "ur", "eadhadh", "iodhadh",
        ],
    },
}


def classify_origin(name):
    """Classify a rune name into its origin system."""
    name_lower = name.lower().strip()
    for system_key, system in RUNE_ORIGINS.items():
        if name_lower in system["runes"]:
            return {
                "system": system_key,
                "name": system["name"],
                "era": system["era"],
                "region": system["region"],
            }
    return {"system": "unknown", "name": "Unknown", "era": "unknown", "region": "unknown"}


def get_origin_system(system_key):
    """Get details of an origin system by key."""
    return RUNE_ORIGINS.get(system_key)


def list_systems():
    """List all known origin systems."""
    return list(RUNE_ORIGINS.keys())


def runes_from_system(system_key):
    """Get all rune names from a specific system."""
    system = RUNE_ORIGINS.get(system_key, {})
    return list(system.get("runes", []))


def era_runes(era):
    """Get all rune names from a specific era."""
    results = []
    for system in RUNE_ORIGINS.values():
        if system["era"] == era:
            results.extend(system["runes"])
    return results


def region_systems(region):
    """Get origin systems from a specific region."""
    return [
        key for key, system in RUNE_ORIGINS.items()
        if system["region"] == region
    ]

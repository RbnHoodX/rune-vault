"""Rune symbolism and correspondence tables."""

ELEMENTAL_ASSOCIATIONS = {
    "fire": {
        "quality": "transformative",
        "direction": "south",
        "season": "summer",
        "runes": ["fehu", "thurisaz", "kenaz", "sowilo", "dagaz"],
    },
    "water": {
        "quality": "intuitive",
        "direction": "west",
        "season": "autumn",
        "runes": ["hagalaz", "isa", "laguz"],
    },
    "earth": {
        "quality": "stabilizing",
        "direction": "north",
        "season": "winter",
        "runes": ["uruz", "wunjo", "jera", "berkano", "othala"],
    },
    "air": {
        "quality": "intellectual",
        "direction": "east",
        "season": "spring",
        "runes": ["ansuz", "raidho", "gebo", "algiz", "tiwaz", "mannaz"],
    },
}

PLANETARY_RULERSHIP = {
    "fehu": "venus",
    "uruz": "mars",
    "thurisaz": "mars",
    "ansuz": "mercury",
    "raidho": "mercury",
    "kenaz": "venus",
    "gebo": "venus",
    "wunjo": "jupiter",
    "hagalaz": "saturn",
    "isa": "saturn",
    "jera": "jupiter",
    "algiz": "moon",
    "sowilo": "sun",
    "tiwaz": "mars",
    "berkano": "moon",
    "mannaz": "mercury",
    "laguz": "moon",
    "dagaz": "sun",
    "othala": "saturn",
}

COLOR_ASSOCIATIONS = {
    "fehu": "gold",
    "uruz": "dark green",
    "thurisaz": "bright red",
    "ansuz": "dark blue",
    "raidho": "bright red",
    "kenaz": "orange",
    "gebo": "deep blue",
    "wunjo": "yellow",
    "hagalaz": "light blue",
    "isa": "white",
    "jera": "light green",
    "algiz": "gold",
    "sowilo": "white-gold",
    "tiwaz": "bright red",
    "berkano": "dark green",
    "mannaz": "deep red",
    "laguz": "deep green",
    "dagaz": "light blue",
    "othala": "deep yellow",
}


def element_for_rune(name):
    """Get the elemental association for a rune."""
    name_lower = name.lower().strip()
    for element, data in ELEMENTAL_ASSOCIATIONS.items():
        if name_lower in data["runes"]:
            return element
    return None


def planet_for_rune(name):
    """Get the planetary rulership for a rune."""
    return PLANETARY_RULERSHIP.get(name.lower().strip())


def color_for_rune(name):
    """Get the color association for a rune."""
    return COLOR_ASSOCIATIONS.get(name.lower().strip())


def runes_by_planet(planet):
    """Get all runes ruled by a given planet."""
    planet_lower = planet.lower()
    return [name for name, p in PLANETARY_RULERSHIP.items() if p == planet_lower]


def runes_by_element(element):
    """Get all runes associated with an element."""
    data = ELEMENTAL_ASSOCIATIONS.get(element.lower())
    if data:
        return list(data["runes"])
    return []


def seasonal_runes(season):
    """Get runes associated with a given season."""
    results = []
    for data in ELEMENTAL_ASSOCIATIONS.values():
        if data["season"] == season.lower():
            results.extend(data["runes"])
    return results


def full_correspondence(name):
    """Get the full correspondence table for a rune."""
    name_lower = name.lower().strip()
    return {
        "element": element_for_rune(name_lower),
        "planet": planet_for_rune(name_lower),
        "color": color_for_rune(name_lower),
    }

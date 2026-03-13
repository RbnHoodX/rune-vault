"""Rune meaning and interpretation lookup."""

RUNE_MEANINGS = {
    "fehu": {
        "literal": "cattle",
        "concept": "wealth",
        "element": "fire",
        "divination": "prosperity and abundance",
    },
    "uruz": {
        "literal": "aurochs",
        "concept": "strength",
        "element": "earth",
        "divination": "raw power and endurance",
    },
    "thurisaz": {
        "literal": "giant",
        "concept": "protection",
        "element": "fire",
        "divination": "defense and confrontation",
    },
    "ansuz": {
        "literal": "god",
        "concept": "wisdom",
        "element": "air",
        "divination": "communication and insight",
    },
    "raidho": {
        "literal": "ride",
        "concept": "journey",
        "element": "air",
        "divination": "travel and movement",
    },
    "kenaz": {
        "literal": "torch",
        "concept": "knowledge",
        "element": "fire",
        "divination": "creativity and learning",
    },
    "gebo": {
        "literal": "gift",
        "concept": "generosity",
        "element": "air",
        "divination": "partnership and exchange",
    },
    "wunjo": {
        "literal": "joy",
        "concept": "harmony",
        "element": "earth",
        "divination": "happiness and comfort",
    },
    "hagalaz": {
        "literal": "hail",
        "concept": "disruption",
        "element": "water",
        "divination": "sudden change and challenge",
    },
    "isa": {
        "literal": "ice",
        "concept": "stillness",
        "element": "water",
        "divination": "patience and reflection",
    },
    "jera": {
        "literal": "year",
        "concept": "harvest",
        "element": "earth",
        "divination": "reward and natural cycles",
    },
    "algiz": {
        "literal": "elk sedge",
        "concept": "protection",
        "element": "air",
        "divination": "shielding and higher self",
    },
    "sowilo": {
        "literal": "sun",
        "concept": "victory",
        "element": "fire",
        "divination": "success and wholeness",
    },
    "tiwaz": {
        "literal": "the god Tyr",
        "concept": "justice",
        "element": "air",
        "divination": "honor and sacrifice",
    },
    "berkano": {
        "literal": "birch",
        "concept": "growth",
        "element": "earth",
        "divination": "renewal and new beginnings",
    },
    "mannaz": {
        "literal": "human",
        "concept": "self",
        "element": "air",
        "divination": "humanity and social order",
    },
    "laguz": {
        "literal": "water",
        "concept": "flow",
        "element": "water",
        "divination": "intuition and the unconscious",
    },
    "dagaz": {
        "literal": "day",
        "concept": "breakthrough",
        "element": "fire",
        "divination": "transformation and awakening",
    },
    "othala": {
        "literal": "heritage",
        "concept": "ancestry",
        "element": "earth",
        "divination": "inheritance and home",
    },
}


def get_meaning(name):
    """Look up the meaning of a rune by name."""
    return RUNE_MEANINGS.get(name.lower().strip())


def meanings_by_element(element):
    """Get all rune meanings for a given element."""
    return {
        name: data
        for name, data in RUNE_MEANINGS.items()
        if data.get("element") == element
    }


def meanings_by_concept(concept):
    """Find runes matching a concept keyword."""
    concept_lower = concept.lower()
    return {
        name: data
        for name, data in RUNE_MEANINGS.items()
        if concept_lower in data.get("concept", "").lower()
    }


def list_elements():
    """List all unique elements across rune meanings."""
    return sorted({data["element"] for data in RUNE_MEANINGS.values()})


def list_concepts():
    """List all unique concepts across rune meanings."""
    return sorted({data["concept"] for data in RUNE_MEANINGS.values()})

from rune import Rune


class Vault:
    """A collection of runes."""

    def __init__(self):
        self._runes = set()
        self._counter = 0

    def inscribe(self, rune):
        """Add a rune to the vault and assign it an id."""
        self._counter += 1
        rune.id = self._counter
        self._runes.add(rune)
        return rune

    def runes(self):
        """Return a list of all runes in the vault."""
        return list(self._runes)

class Rune:
    """A single rune in the vault."""

    def __init__(self, name=""):
        self.id = 0
        self.name = name
        self.stage = "blank"

    def __repr__(self):
        return f"Rune(id={self.id}, name={self.name!r})"

    def __eq__(self, other):
        if not isinstance(other, Rune):
            return NotImplemented
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

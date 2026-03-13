class Rune:
    """A single rune in the vault."""

    def __init__(self, name=""):
        self._id = 0
        self._name = name
        self.stage = "blank"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return f"Rune(id={self._id}, name={self._name!r})"

    def __eq__(self, other):
        if not isinstance(other, Rune):
            return NotImplemented
        return self._id == other._id

    def __hash__(self):
        return hash(self._id)

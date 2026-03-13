"""Timeline management for rune vault history."""


class TimelineEntry:
    """A single event in the vault timeline."""

    def __init__(self, action, rune_id, details=""):
        self.action = action
        self.rune_id = rune_id
        self.details = details
        self.sequence = 0

    def __repr__(self):
        return f"TimelineEntry({self.action!r}, rune={self.rune_id})"


class Timeline:
    """Ordered history of vault operations."""

    def __init__(self):
        self._entries = []
        self._seq = 0

    def record(self, action, rune_id, details=""):
        """Record an event in the timeline."""
        entry = TimelineEntry(action, rune_id, details)
        self._seq += 1
        entry.sequence = self._seq
        self._entries.append(entry)
        return entry

    def entries(self):
        """Return all timeline entries in order."""
        return list(self._entries)

    def entries_for(self, rune_id):
        """Return entries for a specific rune."""
        return [e for e in self._entries if e.rune_id == rune_id]

    def entries_by_action(self, action):
        """Return entries matching a specific action."""
        return [e for e in self._entries if e.action == action]

    def latest(self, n=10):
        """Return the N most recent entries."""
        return list(self._entries[-n:])

    def count(self):
        """Return total number of entries."""
        return len(self._entries)

    def clear(self):
        """Clear all timeline entries."""
        self._entries.clear()
        self._seq = 0

    def actions_summary(self):
        """Summarize actions by count."""
        summary = {}
        for entry in self._entries:
            summary[entry.action] = summary.get(entry.action, 0) + 1
        return summary

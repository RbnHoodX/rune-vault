"""Unit tests for chronicles modules."""

from chronicles.timeline import Timeline, TimelineEntry
from chronicles.audit import check_id_integrity, vault_fingerprint
from chronicles.statistics import stage_distribution, unique_names_count

from rune import Rune
from vault import Vault


class TestTimeline:
    def test_create_timeline(self):
        t = Timeline()
        assert t.count() == 0

    def test_record_entry(self):
        t = Timeline()
        e = t.record("inscribe", 1, "added fehu")
        assert e.action == "inscribe"
        assert e.rune_id == 1

    def test_sequence_numbers(self):
        t = Timeline()
        e1 = t.record("inscribe", 1)
        e2 = t.record("inscribe", 2)
        assert e1.sequence == 1
        assert e2.sequence == 2

    def test_entries_for_rune(self):
        t = Timeline()
        t.record("inscribe", 1)
        t.record("inscribe", 2)
        t.record("carve", 1)
        assert len(t.entries_for(1)) == 2

    def test_latest(self):
        t = Timeline()
        for i in range(20):
            t.record("inscribe", i)
        assert len(t.latest(5)) == 5


class TestAudit:
    def test_clean_vault(self):
        v = Vault()
        v.inscribe(Rune(name="fehu"))
        issues = check_id_integrity(v)
        assert issues == []

    def test_fingerprint(self):
        v = Vault()
        v.inscribe(Rune(name="fehu"))
        fp = vault_fingerprint(v)
        assert "fehu" in fp


class TestStatistics:
    def test_stage_distribution(self):
        v = Vault()
        v.inscribe(Rune(name="fehu"))
        v.inscribe(Rune(name="uruz"))
        dist = stage_distribution(v)
        assert "blank" in dist
        assert dist["blank"]["count"] == 2

    def test_unique_names(self):
        v = Vault()
        v.inscribe(Rune(name="fehu"))
        v.inscribe(Rune(name="fehu"))
        assert unique_names_count(v) == 1

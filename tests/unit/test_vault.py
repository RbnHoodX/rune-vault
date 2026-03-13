"""Unit tests for the Vault class."""

from rune import Rune
from vault import Vault


class TestVaultCreation:
    def test_empty_vault(self):
        v = Vault()
        assert v.runes() == []

    def test_uses_set(self):
        v = Vault()
        assert isinstance(v._runes, set)

    def test_counter_starts_zero(self):
        v = Vault()
        assert v._counter == 0


class TestVaultInscribe:
    def test_inscribe_returns_rune(self):
        v = Vault()
        r = Rune(name="fehu")
        result = v.inscribe(r)
        assert result is r

    def test_inscribe_assigns_id(self):
        v = Vault()
        r = Rune(name="fehu")
        v.inscribe(r)
        assert r.id == 1

    def test_inscribe_increments_id(self):
        v = Vault()
        r1 = Rune(name="fehu")
        r2 = Rune(name="uruz")
        v.inscribe(r1)
        v.inscribe(r2)
        assert r1.id == 1
        assert r2.id == 2

    def test_inscribe_adds_to_vault(self):
        v = Vault()
        r = Rune(name="fehu")
        v.inscribe(r)
        assert r in v.runes()

    def test_runes_returns_list(self):
        v = Vault()
        assert isinstance(v.runes(), list)

    def test_multiple_inscribe(self):
        v = Vault()
        for name in ["fehu", "uruz", "ansuz"]:
            v.inscribe(Rune(name=name))
        assert len(v.runes()) == 3

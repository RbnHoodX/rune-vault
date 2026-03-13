"""Unit tests for storage modules."""

from rune import Rune
from vault import Vault
from storage.serializer import rune_to_dict, vault_to_dict, rune_from_dict, vault_from_dict


class TestSerializer:
    def test_rune_to_dict(self):
        r = Rune(name="fehu")
        r.id = 1
        d = rune_to_dict(r)
        assert d["id"] == 1
        assert d["name"] == "fehu"
        assert d["stage"] == "blank"

    def test_rune_from_dict(self):
        d = {"id": 5, "name": "uruz", "stage": "carved"}
        r = rune_from_dict(d)
        assert r.id == 5
        assert r.name == "uruz"
        assert r.stage == "carved"

    def test_vault_to_dict(self):
        v = Vault()
        v.inscribe(Rune(name="fehu"))
        d = vault_to_dict(v)
        assert "runes" in d
        assert len(d["runes"]) == 1

    def test_vault_from_dict(self):
        d = {"runes": [
            {"id": 1, "name": "fehu", "stage": "blank"},
            {"id": 2, "name": "uruz", "stage": "carved"},
        ]}
        v = vault_from_dict(d)
        assert len(v.runes()) == 2

    def test_roundtrip(self):
        v = Vault()
        v.inscribe(Rune(name="fehu"))
        v.inscribe(Rune(name="uruz"))
        d = vault_to_dict(v)
        v2 = vault_from_dict(d)
        assert len(v2.runes()) == 2

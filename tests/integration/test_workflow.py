"""Integration tests for vault workflows."""

from rune import Rune
from vault import Vault
from storage.serializer import vault_to_dict, vault_from_dict
from chronicles.audit import full_audit


class TestVaultWorkflow:
    def test_create_and_retrieve(self):
        v = Vault()
        r = v.inscribe(Rune(name="fehu"))
        runes = v.runes()
        assert r in runes
        assert r.id == 1

    def test_multiple_runes_unique_ids(self):
        v = Vault()
        ids = set()
        for name in ["fehu", "uruz", "ansuz", "kenaz", "wunjo"]:
            r = v.inscribe(Rune(name=name))
            ids.add(r.id)
        assert len(ids) == 5

    def test_serialize_and_restore(self):
        v = Vault()
        v.inscribe(Rune(name="fehu"))
        v.inscribe(Rune(name="uruz"))

        data = vault_to_dict(v)
        v2 = vault_from_dict(data)

        assert len(v2.runes()) == 2
        names = {r.name for r in v2.runes()}
        assert "fehu" in names
        assert "uruz" in names

    def test_audit_passes(self):
        v = Vault()
        for name in ["fehu", "uruz", "ansuz"]:
            v.inscribe(Rune(name=name))
        report = full_audit(v)
        assert report["clean"] is True

    def test_rune_equality_in_vault(self):
        v = Vault()
        r1 = v.inscribe(Rune(name="fehu"))
        r2 = v.inscribe(Rune(name="uruz"))
        assert r1 != r2
        assert r1 in v.runes()


class TestRuneStages:
    def test_initial_stage(self):
        r = Rune(name="fehu")
        assert r.stage == "blank"

    def test_stage_change(self):
        r = Rune(name="fehu")
        r.stage = "carved"
        assert r.stage == "carved"

    def test_stage_preserved_in_vault(self):
        v = Vault()
        r = Rune(name="fehu")
        r.stage = "carved"
        v.inscribe(r)
        found = [x for x in v.runes() if x.name == "fehu"][0]
        assert found.stage == "carved"

"""Integration tests for data pipeline operations."""

from rune import Rune
from vault import Vault
from utils.search import find_by_name, find_by_stage, count_by_stage
from utils.sorting import sort_by_name, group_by_stage
from utils.formatting import format_rune, format_table


class TestSearchPipeline:
    def test_search_and_format(self):
        v = Vault()
        v.inscribe(Rune(name="fehu"))
        v.inscribe(Rune(name="uruz"))
        v.inscribe(Rune(name="fire rune"))

        results = find_by_name(v, "f")
        assert len(results) == 2

        formatted = [format_rune(r) for r in results]
        assert all("f" in f.lower() for f in formatted)

    def test_filter_and_sort(self):
        v = Vault()
        v.inscribe(Rune(name="Uruz"))
        v.inscribe(Rune(name="ansuz"))
        v.inscribe(Rune(name="Fehu"))

        results = find_by_stage(v, "blank")
        sorted_results = sort_by_name(results)
        names = [r.name for r in sorted_results]
        assert names == ["ansuz", "Fehu", "Uruz"]

    def test_group_and_count(self):
        v = Vault()
        r1 = v.inscribe(Rune(name="fehu"))
        r2 = v.inscribe(Rune(name="uruz"))
        r1.stage = "carved"

        counts = count_by_stage(v)
        assert counts.get("blank") == 1
        assert counts.get("carved") == 1

        groups = group_by_stage(v.runes())
        assert len(groups["blank"]) == 1
        assert len(groups["carved"]) == 1

    def test_table_output(self):
        v = Vault()
        v.inscribe(Rune(name="fehu"))
        v.inscribe(Rune(name="uruz"))

        table = format_table(v.runes())
        assert "ID" in table
        assert "NAME" in table
        assert "fehu" in table

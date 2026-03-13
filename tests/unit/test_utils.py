"""Unit tests for utility modules."""

from rune import Rune
from vault import Vault
from utils.formatting import format_rune, truncate, format_count
from utils.validation import validate_name, is_valid_name, sanitize_text
from utils.sorting import sort_by_name, sort_by_id, partition


class TestFormatting:
    def test_format_rune_with_id(self):
        r = Rune(name="fehu")
        r.id = 1
        result = format_rune(r)
        assert "[1]" in result
        assert "fehu" in result

    def test_format_rune_without_id(self):
        r = Rune(name="fehu")
        r.id = 1
        result = format_rune(r, show_id=False)
        assert "[1]" not in result
        assert "fehu" in result

    def test_truncate_short(self):
        assert truncate("hello", 10) == "hello"

    def test_truncate_long(self):
        result = truncate("a" * 50, 10)
        assert len(result) == 10
        assert result.endswith("...")

    def test_format_count_singular(self):
        assert format_count(1, "rune") == "1 rune"

    def test_format_count_plural(self):
        assert format_count(3, "rune") == "3 runes"


class TestValidation:
    def test_validate_name_valid(self):
        assert validate_name("fehu") == "fehu"

    def test_validate_name_strips(self):
        assert validate_name("  fehu  ") == "fehu"

    def test_validate_name_empty(self):
        import pytest
        with pytest.raises(ValueError):
            validate_name("")

    def test_validate_name_blank(self):
        import pytest
        with pytest.raises(ValueError):
            validate_name("   ")

    def test_is_valid_name(self):
        assert is_valid_name("fehu") is True
        assert is_valid_name("") is False

    def test_sanitize_text(self):
        assert sanitize_text("  hello   world  ") == "hello world"


class TestSorting:
    def test_sort_by_name(self):
        runes = [Rune(name="Uruz"), Rune(name="ansuz"), Rune(name="Fehu")]
        result = sort_by_name(runes)
        assert [r.name for r in result] == ["ansuz", "Fehu", "Uruz"]

    def test_sort_by_id(self):
        r1, r2, r3 = Rune(name="a"), Rune(name="b"), Rune(name="c")
        r1.id, r2.id, r3.id = 3, 1, 2
        result = sort_by_id([r1, r2, r3])
        assert [r.id for r in result] == [1, 2, 3]

    def test_partition(self):
        runes = [Rune(name="fehu"), Rune(name=""), Rune(name="uruz")]
        named, unnamed = partition(runes, lambda r: bool(r.name))
        assert len(named) == 2
        assert len(unnamed) == 1

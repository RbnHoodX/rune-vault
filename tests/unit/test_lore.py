"""Unit tests for lore modules."""

from lore.origins import classify_origin, list_systems, runes_from_system
from lore.meanings import get_meaning, meanings_by_element, list_elements
from lore.inscriptions import detect_script, validate_inscription, word_count


class TestOrigins:
    def test_classify_known_rune(self):
        result = classify_origin("fehu")
        assert result["system"] == "elder_futhark"
        assert result["era"] == "ancient"

    def test_classify_unknown_rune(self):
        result = classify_origin("xyzzy")
        assert result["system"] == "unknown"

    def test_list_systems(self):
        systems = list_systems()
        assert "elder_futhark" in systems
        assert "ogham" in systems

    def test_runes_from_system(self):
        runes = runes_from_system("elder_futhark")
        assert "fehu" in runes
        assert len(runes) == 24


class TestMeanings:
    def test_get_known_meaning(self):
        m = get_meaning("fehu")
        assert m is not None
        assert m["concept"] == "wealth"

    def test_get_unknown_meaning(self):
        m = get_meaning("xyzzy")
        assert m is None

    def test_meanings_by_element(self):
        fire = meanings_by_element("fire")
        assert "fehu" in fire
        assert "sowilo" in fire

    def test_list_elements(self):
        elements = list_elements()
        assert "fire" in elements
        assert "water" in elements


class TestInscriptions:
    def test_detect_latin(self):
        assert detect_script("hello world") == "latin"

    def test_detect_empty(self):
        assert detect_script("") == "unknown"

    def test_validate_inscription(self):
        result = validate_inscription("  hello  ")
        assert result == "hello"

    def test_validate_empty(self):
        import pytest
        with pytest.raises(ValueError):
            validate_inscription("")

    def test_word_count(self):
        assert word_count("hello world") == 2
        assert word_count("") == 0

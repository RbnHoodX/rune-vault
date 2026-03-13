"""Unit tests for the Rune class."""

from rune import Rune


class TestRuneCreation:
    def test_default_name(self):
        r = Rune()
        assert r.name == ""

    def test_custom_name(self):
        r = Rune(name="fehu")
        assert r.name == "fehu"

    def test_default_id(self):
        r = Rune()
        assert r.id == 0

    def test_id_setter(self):
        r = Rune()
        r.id = 42
        assert r.id == 42

    def test_default_stage(self):
        r = Rune()
        assert r.stage == "blank"

    def test_stage_setter(self):
        r = Rune()
        r.stage = "carved"
        assert r.stage == "carved"


class TestRuneRepr:
    def test_repr_format(self):
        r = Rune(name="fehu")
        assert repr(r) == "Rune(id=0, name='fehu')"

    def test_repr_with_id(self):
        r = Rune(name="uruz")
        r.id = 5
        assert repr(r) == "Rune(id=5, name='uruz')"

    def test_repr_empty_name(self):
        r = Rune()
        assert repr(r) == "Rune(id=0, name='')"


class TestRuneEquality:
    def test_equal_by_id(self):
        a = Rune(name="fehu")
        b = Rune(name="uruz")
        a.id = 1
        b.id = 1
        assert a == b

    def test_not_equal_different_id(self):
        a = Rune(name="fehu")
        b = Rune(name="fehu")
        a.id = 1
        b.id = 2
        assert a != b

    def test_not_equal_to_non_rune(self):
        r = Rune(name="fehu")
        assert r != "not a rune"

    def test_hash_by_id(self):
        a = Rune(name="fehu")
        b = Rune(name="uruz")
        a.id = 1
        b.id = 1
        assert hash(a) == hash(b)

    def test_usable_in_set(self):
        a = Rune(name="fehu")
        b = Rune(name="uruz")
        a.id = 1
        b.id = 2
        s = {a, b}
        assert len(s) == 2

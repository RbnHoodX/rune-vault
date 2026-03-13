"""Shared test fixtures for the rune vault test suite."""

import pytest

from rune import Rune
from vault import Vault


@pytest.fixture
def empty_vault():
    """An empty vault with no runes."""
    return Vault()


@pytest.fixture
def sample_vault():
    """A vault with several sample runes."""
    vault = Vault()
    names = ["fehu", "uruz", "thurisaz", "ansuz", "raidho", "kenaz", "gebo"]
    for name in names:
        rune = Rune(name=name)
        vault.inscribe(rune)
    return vault


@pytest.fixture
def single_rune():
    """A single uninscribed rune."""
    return Rune(name="algiz")


@pytest.fixture
def blank_rune():
    """A rune with default (blank) values."""
    return Rune()

"""Validate vault integrity and report issues."""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vault import Vault
from rune import Rune
from chronicles.audit import full_audit, vault_fingerprint


def create_test_vault():
    """Create a vault for validation testing."""
    vault = Vault()
    names = ["fehu", "uruz", "ansuz", "kenaz", "wunjo"]
    for name in names:
        rune = Rune(name=name)
        vault.inscribe(rune)
    return vault


def run_validation():
    """Run validation checks and print results."""
    vault = create_test_vault()

    print("Running vault validation...")
    print(f"Vault contains {len(vault.runes())} runes")
    print()

    report = full_audit(vault)
    if report["clean"]:
        print("All checks passed!")
    else:
        print(f"Found {report['total_issues']} issues:")
        for key in ["id_issues", "name_issues", "stage_issues"]:
            for issue in report[key]:
                print(f"  - {issue}")

    print()
    fingerprint = vault_fingerprint(vault)
    print(f"Vault fingerprint: {fingerprint[:60]}...")


def main():
    run_validation()


if __name__ == "__main__":
    main()

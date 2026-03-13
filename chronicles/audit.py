"""Audit trail and integrity checking for the vault."""


def check_id_integrity(vault):
    """Verify all rune IDs are unique and positive."""
    ids = set()
    issues = []
    for rune in vault.runes():
        if rune.id <= 0:
            issues.append(f"Non-positive ID: {rune.id} ({rune.name})")
        if rune.id in ids:
            issues.append(f"Duplicate ID: {rune.id}")
        ids.add(rune.id)
    return issues


def check_name_integrity(vault):
    """Verify all runes have non-empty names."""
    issues = []
    for rune in vault.runes():
        if not rune.name or not rune.name.strip():
            issues.append(f"Blank name on rune ID {rune.id}")
    return issues


def check_stage_integrity(vault):
    """Verify all runes have valid stages."""
    from config import RUNE_STAGES
    issues = []
    for rune in vault.runes():
        if rune.stage not in RUNE_STAGES:
            issues.append(f"Invalid stage {rune.stage!r} on rune ID {rune.id}")
    return issues


def full_audit(vault):
    """Run all integrity checks and return a report."""
    report = {
        "id_issues": check_id_integrity(vault),
        "name_issues": check_name_integrity(vault),
        "stage_issues": check_stage_integrity(vault),
    }
    report["total_issues"] = sum(len(v) for v in report.values())
    report["clean"] = report["total_issues"] == 0
    return report


def vault_fingerprint(vault):
    """Generate a simple fingerprint of vault state."""
    runes = sorted(vault.runes(), key=lambda r: r.id)
    parts = [f"{r.id}:{r.name}:{r.stage}" for r in runes]
    return "|".join(parts)


def compare_vaults(vault_a, vault_b):
    """Compare two vaults and report differences."""
    runes_a = {r.id: r for r in vault_a.runes()}
    runes_b = {r.id: r for r in vault_b.runes()}

    only_a = set(runes_a.keys()) - set(runes_b.keys())
    only_b = set(runes_b.keys()) - set(runes_a.keys())
    common = set(runes_a.keys()) & set(runes_b.keys())

    changed = []
    for rid in common:
        ra, rb = runes_a[rid], runes_b[rid]
        if ra.name != rb.name or ra.stage != rb.stage:
            changed.append(rid)

    return {
        "only_in_a": sorted(only_a),
        "only_in_b": sorted(only_b),
        "changed": sorted(changed),
        "identical": len(common) - len(changed),
    }

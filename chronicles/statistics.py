"""Statistical analysis of vault contents."""


def stage_distribution(vault):
    """Calculate the distribution of runes across stages."""
    dist = {}
    runes = vault.runes()
    total = len(runes)
    for r in runes:
        dist[r.stage] = dist.get(r.stage, 0) + 1

    result = {}
    for stage, count in sorted(dist.items()):
        result[stage] = {
            "count": count,
            "percentage": (count / total * 100) if total > 0 else 0,
        }
    return result


def name_length_stats(vault):
    """Calculate statistics about rune name lengths."""
    runes = vault.runes()
    if not runes:
        return {"min": 0, "max": 0, "avg": 0, "total": 0}

    lengths = [len(r.name) for r in runes]
    return {
        "min": min(lengths),
        "max": max(lengths),
        "avg": sum(lengths) / len(lengths),
        "total": len(lengths),
    }


def unique_names_count(vault):
    """Count the number of unique rune names."""
    return len({r.name for r in vault.runes()})


def stage_transition_rate(vault):
    """Calculate what percentage of runes have moved past blank stage."""
    runes = vault.runes()
    if not runes:
        return 0.0
    advanced = sum(1 for r in runes if r.stage != "blank")
    return (advanced / len(runes)) * 100


def vault_summary(vault):
    """Generate a comprehensive vault summary."""
    runes = vault.runes()
    return {
        "total_runes": len(runes),
        "unique_names": unique_names_count(vault),
        "stage_distribution": stage_distribution(vault),
        "name_stats": name_length_stats(vault),
        "transition_rate": stage_transition_rate(vault),
    }


def most_common_names(vault, n=5):
    """Find the N most common rune names."""
    counts = {}
    for r in vault.runes():
        counts[r.name] = counts.get(r.name, 0) + 1
    sorted_names = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_names[:n]

"""Command-line interface for the rune vault system."""

import sys

from vault import Vault
from rune import Rune
from config import APP_NAME, VERSION, SUPPORTED_EXPORT_FORMATS


def parse_args(argv):
    """Parse command-line arguments into a structured dict."""
    result = {
        "command": None,
        "options": {},
        "positional": [],
    }

    if not argv:
        result["command"] = "help"
        return result

    result["command"] = argv[0]
    rest = argv[1:]

    i = 0
    while i < len(rest):
        arg = rest[i]
        if arg.startswith("--"):
            key = arg[2:]
            if i + 1 < len(rest) and not rest[i + 1].startswith("--"):
                result["options"][key] = rest[i + 1]
                i += 2
            else:
                result["options"][key] = True
                i += 1
        else:
            result["positional"].append(arg)
            i += 1

    return result


def format_help():
    """Return help text for the CLI."""
    lines = [
        f"{APP_NAME} v{VERSION}",
        "",
        "Commands:",
        "  list                 List all runes in the vault",
        "  add <name>           Add a new rune to the vault",
        "  info <id>            Show details of a specific rune",
        "  search <pattern>     Search runes by name",
        "  stats                Show vault statistics",
        "  stages               List all valid rune stages",
        "  export [--format f]  Export vault data",
        "  help                 Show this help message",
        "",
        "Options:",
        "  --format <format>    Export format (text, csv, json)",
        "  --verbose            Show detailed output",
        "  --limit <n>          Limit number of results",
    ]
    return "\n".join(lines)


def run(command, vault, options=None, positional=None):
    """Execute a CLI command against the vault."""
    options = options or {}
    positional = positional or []

    if command == "help":
        return format_help()

    if command == "list":
        runes = vault.runes()
        if not runes:
            return "Vault is empty."
        limit = int(options.get("limit", 0))
        if limit > 0:
            runes = runes[:limit]
        lines = [repr(r) for r in runes]
        return "\n".join(lines)

    if command == "add":
        if not positional:
            return "Error: name required"
        name = " ".join(positional)
        rune = Rune(name=name)
        vault.inscribe(rune)
        return f"Added: {rune!r}"

    if command == "info":
        if not positional:
            return "Error: id required"
        target_id = int(positional[0])
        for r in vault.runes():
            if r.id == target_id:
                lines = [
                    f"ID: {r.id}",
                    f"Name: {r.name}",
                    f"Stage: {r.stage}",
                ]
                return "\n".join(lines)
        return f"Error: rune {target_id} not found"

    if command == "search":
        if not positional:
            return "Error: pattern required"
        pattern = positional[0].lower()
        matches = [r for r in vault.runes() if pattern in r.name.lower()]
        if not matches:
            return "No matches found."
        return "\n".join(repr(r) for r in matches)

    if command == "stats":
        runes = vault.runes()
        stages = {}
        for r in runes:
            stages[r.stage] = stages.get(r.stage, 0) + 1
        lines = [
            f"Total runes: {len(runes)}",
            "By stage:",
        ]
        for stage, count in sorted(stages.items()):
            lines.append(f"  {stage}: {count}")
        return "\n".join(lines)

    if command == "stages":
        from config import RUNE_STAGES
        return "\n".join(RUNE_STAGES)

    if command == "export":
        fmt = options.get("format", "text")
        if fmt not in SUPPORTED_EXPORT_FORMATS:
            return f"Error: unsupported format '{fmt}'"
        return f"Exported vault in {fmt} format."

    return f"Error: unknown command '{command}'"


def main():
    """Entry point for the CLI."""
    args = parse_args(sys.argv[1:])
    vault = Vault()
    result = run(args["command"], vault, args["options"], args["positional"])
    print(result)


if __name__ == "__main__":
    main()

def main() -> None:
    print("=== Kaboom 1 ===")
    print("Secretly importing dark_spellbook directly")
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    print("Testing record dark spell...")
    dark_spellbook.dark_spell_record(
        "Necro-Flare",
        "bats, frogs, arsenic",
    )


if __name__ == "__main__":
    main()

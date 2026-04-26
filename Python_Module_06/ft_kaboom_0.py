import alchemy.grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    record = alchemy.grimoire.light_spell_record(
        "Fantasy",
        "Earth, wind and fire",
    )
    print(
        "Testing record light spell: "
        f"{record}"
    )


if __name__ == "__main__":
    main()

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True,
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    max_power = max(mages, key=lambda mage: mage["power"])["power"]
    min_power = min(mages, key=lambda mage: mage["power"])["power"]
    avg_power = round(
        sum(map(lambda mage: mage["power"], mages)) / len(mages),
        2,
    )

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power,
    }


if __name__ == "__main__":
    sample_artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Wind Charm", "power": 73, "type": "trinket"},
    ]
    sample_mages = [
        {"name": "Ayla", "power": 98, "element": "fire"},
        {"name": "Rin", "power": 67, "element": "water"},
        {"name": "Zed", "power": 82, "element": "air"},
    ]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(sample_artifacts)
    print(
        f"{sorted_artifacts[0]['name']} "
        f"({sorted_artifacts[0]['power']} power) "
        f"comes before {sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )

    print("Testing spell transformer...")
    print(" ".join(spell_transformer(["fireball", "heal", "shield"])))

    print("Testing power filter...")
    print(power_filter(sample_mages, 80))

    print("Testing mage stats...")
    print(mage_stats(sample_mages))

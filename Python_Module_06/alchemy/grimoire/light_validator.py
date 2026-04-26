from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = set(light_spell_allowed_ingredients())
    normalized = [
        token.strip().lower()
        for token in ingredients.replace(",", " ").split()
        if token.strip()
    ]
    status = (
        "VALID"
        if any(token in allowed_ingredients for token in normalized)
        else "INVALID"
    )
    return f"{ingredients} - {status}"

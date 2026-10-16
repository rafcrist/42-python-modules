from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    lowered = ingredients.lower()
    allowed = dark_spell_allowed_ingredients()
    status = "VALID" if any(item in lowered for item in allowed) else "INVALID"
    return f"{ingredients} - {status}"

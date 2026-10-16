def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    lowered = ingredients.lower()
    allowed = light_spell_allowed_ingredients()
    status = "VALID" if any(item in lowered for item in allowed) else "INVALID"
    return f"{ingredients} - {status}"

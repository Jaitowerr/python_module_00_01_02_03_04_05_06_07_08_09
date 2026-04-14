from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    valid = any(i in ingredients.lower() for i in allowed)
    keyword = "VALID" if valid else "INVALID"
    return f"{ingredients} - {keyword}"

# Баланс игры
RESOURCES = {
    "start_gold": (100, 200),
    "start_food": (150, 300),
    "start_army": (20, 50)
}

EVENT_CHANCES = {
    "disaster": 15,
    "positive": 30,
    "neutral": 55
}

TRAITS = [
    ("Щедрый", "gold", -10, "prosperity", +5),
    ("Скупой", "gold", +15, "prosperity", -7),
    ("Воинственный", "army", +20, "food", -30)
]
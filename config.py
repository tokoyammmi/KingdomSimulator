RESOURCES = {
    "start_gold": (100, 200),
    "start_food": (150, 300),
    "start_army": (20, 50)
}

TRAITS = [
    ("Щедрый", "gold", -10, "prosperity", +5),
    ("Скупой", "gold", +15, "prosperity", -7),
    ("Воинственный", "army", +20, "food", -30)
]

TECHNOLOGIES = [
    {
        "name": "Трёхпольная система",
        "effects": {"food": 0.3},
        "cost": {"gold": 50, "years": 2}
    },
    {
        "name": "Стальная металлургия",
        "effects": {"army": 0.2},
        "cost": {"gold": 100, "years": 3},
        "requirements": ["Трёхпольная система"]
    }
]

EVENT_VARIATIONS = {
    "monsters": ["орки", "гоблины", "тролли", "нежить"],
    "locations": ["леса", "горы", "долины", "болота"],
    "resources": ["золото", "еда", "армия"]
}
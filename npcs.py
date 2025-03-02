import random  # Добавляем импорт модуля

NPC_DATABASE = {
    "blacksmith": {
        "name": "Грон Железный Кулак",
        "dialogs": {
            "greeting": [
                "Кузница горит, мой король! Нужно больше {material}!",
                "Доспехи для стражи требуют обновления..."
            ],
            "requests": {
                "material": ["стали", "золота", "мифрила"],
                "actions": {
                    "1": {"text": "Выделить ресурсы", "effect": {"gold": -50, "army": +20}},
                    "2": {"text": "Отказать", "effect": {"prosperity": -10}}
                }
            }
        }
    }
}

def generate_npc_event():
    npc = random.choice(list(NPC_DATABASE.values()))  # Теперь random доступен
    dialog_template = random.choice(npc["dialogs"]["greeting"])
    material = random.choice(npc["dialogs"]["requests"]["material"])
    
    return {
        "text": dialog_template.format(material=material),
        "options": {
            k: {"action": v["text"], "effects": v["effect"]} 
            for k, v in npc["dialogs"]["requests"]["actions"].items()
        }
    }
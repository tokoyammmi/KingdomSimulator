import random
from colorama import Fore

EVENT_TEMPLATES = {
    "crisis": {
        "weight": 40,
        "templates": [
            {
                "type": "rebellion",
                "text": "Недовольство среди {group} из-за {reason}",
                "vars": {
                    "group": ["крестьян", "дворян", "торговцев"],
                    "reason": ["налогов", "голода", "эпидемии"]
                },
                "options": {
                    "1": {
                        "action": "Жестко подавить", 
                        "effects": {"resources": {"army": -20}, "prosperity": -15}
                    },
                    "2": {
                        "action": "Пойти на уступки", 
                        "effects": {"resources": {"gold": -50}, "prosperity": +10}
                    }
                }
            }
        ]
    },
    "opportunity": {
        "weight": 35,
        "templates": [
            {
                "type": "trade",
                "text": "{trader} предлагает выгодную сделку",
                "vars": {
                    "trader": ["Купеческий караван", "Иностранные послы", "Гномьи торговцы"]
                },
                "options": {
                    "1": {
                        "action": "Принять предложение", 
                        "effects": {"resources": {"gold": 100}, "prosperity": +5}
                    },
                    "2": {
                        "action": "Отказаться", 
                        "effects": {"prosperity": -5}
                    }
                }
            }
        ]
    }
}

def generate_event():
    event_type = random.choices(
        list(EVENT_TEMPLATES.keys()),
        weights=[t["weight"] for t in EVENT_TEMPLATES.values()],
        k=1
    )[0]
    
    template = random.choice(EVENT_TEMPLATES[event_type]["templates"])
    variables = {k: random.choice(v) for k, v in template["vars"].items()}
    
    return {
        "text": template["text"].format(**variables),
        "options": {
            k: {
                "action": v["action"],
                "effects": v["effects"]
            } for k, v in template["options"].items()
        }
    }
import random
from colorama import Fore, Style

def generate_event(game):
    events = [
        {
            "type": "disaster",
            "text": f"{Fore.RED}🐀 Нашествие крыс атакует амбары!{Style.RESET_ALL}",
            "comment": "Голодные грызуны уничтожают ваши запасы,\nно вы можете попытаться сократить потери.",
            "options": {
                "1": {
                    "action": f"{Fore.GREEN}Мобилизовать народ на борьбу{Style.RESET_ALL}",
                    "effects": {
                        "resources": {"food": -0.2, "gold": -30},
                        "stats": {"prosperity": 5}
                    },
                    "consequences": [
                        "Народ работает день и ночь, сохраняя часть запасов",
                        "Казна истощена организацией работ"
                    ]
                },
                "2": {
                    "action": f"{Fore.RED}Проигнорировать проблему{Style.RESET_ALL}",
                    "effects": {
                        "resources": {"food": -0.5}
                    },
                    "consequences": [
                        "Крысы размножаются в геометрической прогрессии",
                        "Потеряно половина продовольствия"
                    ]
                }
            }
        },
        {
            "type": "diplomacy",
            "text": f"{Fore.CYAN}👑 Посол {random.choice(['Эльфийских земель', 'Гномьих кланов', 'Людских княжеств'])} требует аудиенции!{Style.RESET_ALL}",
            "comment": "Иностранная делегация прибыла с важными предложениями,\nно их намерения не до конца ясны.",
            "options": {
                "1": {
                    "action": f"{Fore.BLUE}Выслушать предложение{Style.RESET_ALL}",
                    "effects": {
                        "resources": {"gold": 120},
                        "stats": {"relations": {"соседи": 20}}
                    },
                    "consequences": [
                        "Заключен выгодный торговый договор",
                        "В казну поступает золото в обмен на торговые привилегии"
                    ]
                },
                "2": {
                    "action": f"{Fore.YELLOW}Отложить переговоры{Style.RESET_ALL}",
                    "effects": {
                        "stats": {"prosperity": -10}
                    },
                    "consequences": [
                        "Посольство уезжает недовольным",
                        "Репутация королевства страдает"
                    ]
                },
                "3": {
                    "action": f"{Fore.RED}Арестовать посла{Style.RESET_ALL}",
                    "effects": {
                        "resources": {"army": -15},
                        "stats": {"relations": {"соседи": -40}}
                    },
                    "consequences": [
                        "Международный скандал!",
                        "Армия теряет боевой дух от позорного приказа"
                    ]
                }
            }
        }
    ]
    return random.choice(events)
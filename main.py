from colorama import Fore, Style, init
from game_state import GameState
from events import generate_event
from interface import TerminalInterface
import random

init()
ui = TerminalInterface()

def apply_effects(game, effects):
    """Применение эффектов к игровому состоянию"""
    # Обработка ресурсов
    if "resources" in effects:
        for res, val in effects["resources"].items():
            game.resources[res] += val
            game.resources[res] = max(0, game.resources[res])
    
    # Обработка процветания
    if "prosperity" in effects:
        game.kingdom.prosperity += effects["prosperity"]
        game.kingdom.prosperity = max(0, min(100, game.kingdom.prosperity))

def main():
    game = GameState()
    
    try:
        while True:
            ui.clear()
            
            # Генерация события
            event = generate_event()
            
            # Отображение интерфейса
            ui.show_event(event)
            ui.show_status(game.resources, game.kingdom.prosperity, game.kingdom.year)
            
            # Обработка выбора
            if event["options"]:
                choice = input(f"\n{Fore.YELLOW}➜ Введите номер выбора: {Style.RESET_ALL}").strip()
                outcome = event["options"].get(choice, {})
                
                if outcome:
                    apply_effects(game, outcome.get("effects", {}))
                    
                    # Случайный бонус
                    if random.random() < 0.3:
                        bonus = random.choice(["gold", "food", "army"])
                        game.resources[bonus] += random.randint(10, 30)
                        ui.show_event({
                            "text": f"{Fore.MAGENTA}✦ Неожиданный бонус: +{game.resources[bonus]} {bonus}",
                            "options": {}
                        })
            
            # Проверка условий игры
            if game.kingdom.prosperity <= 0:
                ui.show_event({"text": f"{Fore.RED}Королевство пало!", "options": {}})
                break
            elif game.kingdom.prosperity >= 100:
                ui.show_event({"text": f"{Fore.GREEN}Великая империя создана!", "options": {}})
                break
                
            game.kingdom.year += 1
            
    except KeyboardInterrupt:
        ui.show_event({"text": f"{Fore.YELLOW}Игра прервана", "options": {}})
    finally:
        input(f"{Fore.CYAN}\nНажмите Enter для выхода...{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
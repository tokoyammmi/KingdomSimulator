from colorama import init, Fore, Style
from game_state import GameState
from events import generate_event
from utils import show_intro, show_resources
from ascii_art import print_divider

init(autoreset=True)

def handle_event(game, event):
    print_divider()
    print(f"{Fore.WHITE}📅 Год {game.year}{Style.RESET_ALL}")
    print(event["text"])
    
    if "comment" in event:
        print(f"\n{Fore.BLUE}💬 {event['comment']}{Style.RESET_ALL}")
    
    if "options" in event:
        for key, opt in event["options"].items():
            print(f"\n{Fore.MAGENTA}[{key}]{Style.RESET_ALL} {opt['action']}")
            if "consequences" in opt:
                print(f"   {Fore.WHITE}→ {' / '.join(opt['consequences'])}{Style.RESET_ALL}")
        
        choice = input(f"\n{Fore.CYAN}➜ Ваш выбор:{Style.RESET_ALL} ")
        selected = event["options"].get(choice, {})
        
        if selected:
            print(f"\n{Fore.YELLOW}⚖️ Последствия:{Style.RESET_ALL}")
            for consequence in selected.get("consequences", []):
                print(f"   {Fore.WHITE}• {consequence}{Style.RESET_ALL}")
            print_divider()
        
        return selected.get("effects", {})
    else:
        return event.get("effects", {})

def main():
    game = GameState()
    show_intro()
    
    while not game.is_game_over:
        event = generate_event(game)
        outcome = handle_event(game, event)
        
        if outcome:
            # Применение эффектов ресурсов
            for res, val in outcome.get("resources", {}).items():
                if isinstance(val, float):
                    game.resources[res] = int(game.resources[res] * val)
                else:
                    game.resources[res] += val
            
            # Применение эффектов статистики
            for stat_type, values in outcome.get("stats", {}).items():
                if stat_type == "prosperity":
                    game.kingdom.prosperity = max(0, game.kingdom.prosperity + values)
                elif stat_type == "relations":
                    for faction, val in values.items():
                        game.kingdom.relations[faction] = max(-100, min(100, game.kingdom.relations[faction] + val))
            
            # Проверка условий поражения
            defeat_conditions = (
                any(v <= 0 for v in game.resources.values()),
                game.kingdom.prosperity <= 0,
                any(v <= -50 for v in game.kingdom.relations.values())
            )
            
            if any(defeat_conditions):
                print(f"\n{Fore.RED}🔥 Королевство пало! Причины:{Style.RESET_ALL}")
                if defeat_conditions[0]: print(f"{Fore.RED}- Ресурсы истощены{Style.RESET_ALL}")
                if defeat_conditions[1]: print(f"{Fore.RED}- Полный упадок процветания{Style.RESET_ALL}")
                if defeat_conditions[2]: print(f"{Fore.RED}- Вражеская оккупация{Style.RESET_ALL}")
                break
            
            # Проверка победы
            if game.kingdom.prosperity >= 100:
                print(f"\n{Fore.GREEN}🎉 Вы создали великую империю!{Style.RESET_ALL}")
                break
            
            game.year += 1
            show_resources(game.resources, game.kingdom)

if __name__ == "__main__":
    main()
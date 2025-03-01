from colorama import Fore, Style
from ascii_art import print_throne, print_divider

def show_intro():
    print(f"""{Fore.YELLOW}
    ░▒▓███████▓▒░  ░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░  
    ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░       
    ░▒▓█▓▒░      ░ ░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░       
    ░▒▓█▓▒░         ░▒▓███████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░       
    ░▒▓█▓▒░         ░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░       
    ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░       
    ░▒▓███████▓▒░  ░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓██████▓▒░  ░▒▓█▓▒░{Style.RESET_ALL}""")
    print_throne()

def show_resources(resources, kingdom):
    print_divider()
    print(f"{Fore.CYAN}⚖️ Состояние королевства:{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}💰 Золото: {resources['gold']}")
    print(f"{Fore.GREEN}🍞 Продовольствие: {resources['food']}")
    print(f"{Fore.RED}⚔️ Армия: {resources['army']}")
    print(f"{Fore.MAGENTA}📈 Процветание: {kingdom.prosperity}")
    print(f"{Fore.BLUE}🤝 Отношения с соседями: {kingdom.relations['соседи']}{Style.RESET_ALL}")
    print_divider()
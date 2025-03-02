from colorama import Fore, Style  # Добавляем импорт Style

def print_throne():
    print(f"""{Fore.YELLOW}
          ▄████████████▄
         ████████████████
         ██▓▓▓▓▓▓▓▓▓▓▓▓██
         ██▓▓▓▓▓▓▓▓▓▓▓▓██
         ████████████████
    ▄▄▄▄██{Fore.WHITE}▒▒▒▒{Fore.YELLOW}██████{Fore.WHITE}▒▒▒▒{Fore.YELLOW}██▄▄▄▄
    ▀▀▀▀    ▀▀▀▀▀▀▀▀    ▀▀▀▀{Style.RESET_ALL}""")

def print_laboratory():
    print(f"""{Fore.BLUE}
    ╭─────⋆⋅☼⋅⋆─────╮
    │   ░▒▓▌🔬▐▓▒░   │
    ╰─────⋆⋅☼⋅⋆─────╯{Style.RESET_ALL}""")
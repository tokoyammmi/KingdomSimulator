from colorama import Fore, Style

def print_throne():
    print(f"""{Fore.YELLOW}
          ▄████████████▄
         ████████████████
         ██▓▓▓▓▓▓▓▓▓▓▓▓██
         ██▓▓▓▓▓▓▓▓▓▓▓▓██
         ████████████████
    ▄▄▄▄██{Fore.WHITE}▒▒▒▒{Fore.YELLOW}██████{Fore.WHITE}▒▒▒▒{Fore.YELLOW}██▄▄▄▄
    ▀▀▀▀    ▀▀▀▀▀▀▀▀    ▀▀▀▀{Style.RESET_ALL}""")

def print_divider():
    print(f"\n{Fore.BLUE}▬▬ι═══════ﺤ{Style.RESET_ALL}\n")

def print_ambassador():
    print(f"""{Fore.CYAN}
          ╔════════════╗
          ║    ⚜️    ║
          ╚════════════╝
           /░░░░░░░░\\
          /░░░░░░░░░░\\
         /░░░░░░░░░░░░\\{Style.RESET_ALL}""")
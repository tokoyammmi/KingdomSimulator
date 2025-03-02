from colorama import Fore, Style, init
import os

init(autoreset=True)

class TerminalInterface:
    def __init__(self):
        self.screen_width = 80
        
    def clear(self):
        """Очистка экрана"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def show_header(self):
        """Отображение шапки игры"""
        print(f"\n{Fore.YELLOW}╔{'═'*78}╗")
        print(f"║{Fore.WHITE}          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄{Fore.YELLOW}║")
        print(f"║{Fore.WHITE}         █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█{Fore.YELLOW}║")
        print(f"╚{'═'*78}╝")
        print(f"{Fore.CYAN}{'КОРОЛЕВСКАЯ СИМУЛЯЦИЯ 2.1':^80}{Style.RESET_ALL}\n")

    def show_event(self, event):
        """Отображение текущего события"""
        self.clear()
        self.show_header()
        print(f"{Fore.YELLOW}═{' ТЕКУЩЕЕ СОБЫТИЕ ':=^{self.screen_width-2}}═{Style.RESET_ALL}")
        print(f"\n{Fore.WHITE}{event['text']}\n")
        
        for key, option in event["options"].items():
            print(f"{Fore.CYAN}[{key}] {option['action']}{Style.RESET_ALL}")
        
        print(f"\n{Fore.YELLOW}═{' ВАШ ВЫБОР ':=^{self.screen_width-2}}═{Style.RESET_ALL}")

    def show_status(self, resources, prosperity, year):
        """Обновление статусной строки"""
        status_bar = (
            f"{Fore.GREEN}💰: {resources['gold']} | "
            f"🍞: {resources['food']} | "
            f"{Fore.RED}⚔️: {resources['army']} | "
            f"{Fore.BLUE}📈: {prosperity}% | "
            f"📅 Год: {year}"
        )
        print(f"\n{Fore.WHITE}╞{status_bar:═^{self.screen_width-2}}╡{Style.RESET_ALL}")
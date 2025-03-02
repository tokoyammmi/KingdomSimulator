from colorama import Fore, Style
import random

class Technology:
    def __init__(self, name, description, effects, requirements=None):
        self.name = name
        self.description = description
        self.effects = effects
        self.requirements = requirements or []
        self.research_progress = 0
        self.is_researched = False

    def __str__(self):
        status = f"{Fore.GREEN}Изучено{Style.RESET_ALL}" if self.is_researched else f"{Fore.YELLOW}Прогресс: {self.research_progress}%{Style.RESET_ALL}"
        return f"{Fore.CYAN}{self.name}{Style.RESET_ALL}\n{self.description}\n{status}"
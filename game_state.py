from colorama import Fore
import random
from config import RESOURCES, TRAITS, TECHNOLOGIES

class Kingdom:
    def __init__(self):
        self.year = 1
        self.prosperity = random.randint(30, 70)
        self.name = self.generate_name()
        self.relations = {
            "соседи": random.randint(-20, 50),
            "церковь": random.randint(10, 80)
        }

    def generate_name(self):
        prefixes = ["Драконий", "Серебряный", "Железный"]
        suffixes = ["Престол", "Оплот", "Удел"]
        return f"{Fore.MAGENTA}{random.choice(prefixes)} {random.choice(suffixes)}"

class GameState:
    def __init__(self):
        self.kingdom = Kingdom()
        self.resources = {
            "gold": random.randint(*RESOURCES["start_gold"]),
            "food": random.randint(*RESOURCES["start_food"]),
            "army": random.randint(*RESOURCES["start_army"])
        }
        self.technologies = []
        self.current_research = None

    def check_game_over(self):
        if any(v <= 0 for v in self.resources.values()):
            return f"{Fore.RED}Ресурсы истощены! Королевство пало!"
        if self.kingdom.prosperity <= 0:
            return f"{Fore.RED}Народ восстал! Правление окончено!"
        if self.kingdom.prosperity >= 100:
            return f"{Fore.GREEN}Вы создали великую империю! Победа!"
        return None
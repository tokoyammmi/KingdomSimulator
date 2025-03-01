from colorama import Fore, Style
import random
from config import RESOURCES, TRAITS

class Ruler:
    def __init__(self):
        self.name = random.choice(["Аэдриан", "Люция", "Гаррик", "Элвира"])
        self.traits = random.sample(TRAITS, 2)
        self.health = 100
        
class Kingdom:
    def __init__(self):
        self.name = self.generate_name()
        self.prosperity = random.randint(30, 70)
        self.relations = {
            "соседи": random.randint(-20, 50),
            "церковь": random.randint(10, 80)
        }
    
    def generate_name(self):
        prefixes = ["Древнее", "Священное", "Великое"]
        suffixes = ["Королевство", "Царство", "Империя"]
        return f"{Fore.MAGENTA}{random.choice(prefixes)} {random.choice(suffixes)}{Style.RESET_ALL}"

class GameState:
    def __init__(self):
        self.year = 1
        self.ruler = Ruler()
        self.kingdom = Kingdom()
        self.resources = {
            "gold": random.randint(*RESOURCES["start_gold"]),
            "food": random.randint(*RESOURCES["start_food"]),
            "army": random.randint(*RESOURCES["start_army"])
        }
        self.is_game_over = False
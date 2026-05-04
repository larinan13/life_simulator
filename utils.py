# Вспомогательные утилиты для симулятора жизни

import random
from typing import List
from organism import Organism

def random_energy(min_val: float = 10, max_val: float = 100) -> float:
    # Генерирует случайное значение энергии
    return random.uniform(min_val, max_val)

def format_stats(organisms: List[Organism]) -> str:
    # Форматирует статистику по организмам
    if not organisms:
        return "Нет организмов"
    alive = sum(1 for o in organisms if o.is_alive())
    total_energy = sum(o.energy for o in organisms if o.is_alive())
    return f"Живых: {alive}, Общая энергия: {total_energy:.1f}"

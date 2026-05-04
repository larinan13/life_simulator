# Модуль с классами организмов: базовый Organism, Prey (жертва), Predator (хищник)

import random

class Organism:
    # Базовый класс для всех организмов
    
    def __init__(self, name: str, energy: float):
        # Инициализация организма
        # Args:
        #     name: Имя организма
        #     energy: Количество энергии (здоровье)
        self.name = name
        self.energy = energy
    
    def eat(self, food_energy: float) -> None:
        # Увеличивает энергию организма при поедании пищи
        self.energy += food_energy
        print(f"  {self.name} съел {food_energy:.1f} энергии. Теперь энергии: {self.energy:.1f}")
    
    def lose_energy(self, amount: float) -> None:
        # Трата энергии (голод, атака и т.д.)
        self.energy -= amount
        if self.energy < 0:
            self.energy = 0
    
    def is_alive(self) -> bool:
        # Проверяет, жив ли организм (энергия > 0)
        return self.energy > 0
    
    def __str__(self) -> str:
        return f"{self.name} (энергия: {self.energy:.1f})"


class Prey(Organism):
    # Класс жертвы — травоядное, которое может убегать от хищников
    
    def __init__(self, name: str, energy: float, escape_chance: float = 0.5):
        # Args:
        #     name: Имя жертвы
        #     energy: Энергия
        #     escape_chance: Вероятность убежать от хищника (0..1)
        super().__init__(name, energy)
        self.escape_chance = escape_chance
    
    def escape(self) -> bool:
        # Возвращает True, если жертва успешно убежала
        return random.random() < self.escape_chance
    
    def graze(self) -> None:
        # Жертва пасётся и восстанавливает энергию
        food = random.uniform(5, 15)
        self.eat(food)


class Predator(Organism):
    # Класс хищника — охотится на жертв
    
    def __init__(self, name: str, energy: float, hunting_success: float = 0.6):
        # Args:
        #     name: Имя хищника
        #     energy: Энергия
        #     hunting_success: Базовая вероятность успешной охоты (0..1)
        super().__init__(name, energy)
        self.hunting_success = hunting_success
    
    def hunt(self, prey: Prey) -> bool:
        # Охота на конкретную жертву
        # Returns:
        #     True, если охота успешна (жертва съедена)
        
        if not prey.is_alive():
            return False
        
        # Шанс убегания жертвы снижает успех хищника
        success_prob = self.hunting_success * (1 - prey.escape_chance * 0.7)
        if random.random() < success_prob:
            # Хищник съедает жертву
            energy_gain = prey.energy * 0.8  # 80% энергии жертвы
            self.eat(energy_gain)
            prey.lose_energy(prey.energy)  # Жертва умирает
            print(f"    🐺 {self.name} съел {prey.name} и получил {energy_gain:.1f} энергии!")
            return True
        else:
            # Неудачная охота
            self.lose_energy(5)  # Хищник тратит энергию на погоню
            print(f"    ❌ {self.name} не смог поймать {prey.name}. Потеряно 5 энергии.")
            return False

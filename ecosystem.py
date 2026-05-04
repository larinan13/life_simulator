# Модуль экосистемы: управление всеми организмами и их взаимодействиями

from typing import List
from organism import Organism, Prey, Predator

class Ecosystem:
    # Класс, представляющий экосистему с организмами
    
    def __init__(self, name: str = "Экосистема"):
        
        self.name = name
        self.organisms: List[Organism] = []
    
    def add_organism(self, organism: Organism) -> None:
        # Добавляет организм в экосистему
        self.organisms.append(organism)
        print(f"Добавлен {organism.name} в {self.name}")
    
    def remove_dead_organisms(self) -> None:
        # Удаляет мёртвые организмы из списка
        alive_count_before = len(self.organisms)
        self.organisms = [org for org in self.organisms if org.is_alive()]
        removed = alive_count_before - len(self.organisms)
        if removed > 0:
            print(f"  Удалено {removed} мёртвых организмов.")
    
    def has_alive_organisms(self) -> bool:
        # Проверяет, остались ли живые организмы
        return any(org.is_alive() for org in self.organisms)
    
    def simulate_day(self) -> None:
        # Симулирует один день в экосистеме
        print(f"\n🏞️  День в {self.name}")
        
        # 1. Жертвы пасутся (восстанавливают энергию)
        prey_list = [org for org in self.organisms if isinstance(org, Prey) and org.is_alive()]
        for prey in prey_list:
            prey.graze()
        
        # 2. Хищники теряют энергию (голод) и охотятся
        predators = [org for org in self.organisms if isinstance(org, Predator) and org.is_alive()]
        
        for predator in predators:
            # Базовые потери энергии на день
            predator.lose_energy(3)
            if not predator.is_alive():
                print(f"  💀 {predator.name} умер от голода.")
                continue
            
            # Поиск живой жертвы
            available_prey = [p for p in prey_list if p.is_alive()]
            if available_prey:
                # Хищник охотится на первую доступную жертву
                target = available_prey[0]
                predator.hunt(target)
            else:
                print(f"  🍂 {predator.name} не нашёл жертв и голодает.")
        
        # 3. Все организмы теряют немного энергии на поддержание жизни
        for org in self.organisms:
            if org.is_alive():
                org.lose_energy(1)
                if not org.is_alive():
                    print(f"  💀 {org.name} умер от истощения.")
        
        # 4. Удаляем мёртвых
        self.remove_dead_organisms()
    
    def show_status(self) -> None:
        # Показывает текущее состояние экосистемы
        if not self.organisms:
            print("  В экосистеме нет живых организмов.")
            return
        
        print("\n📊 Текущее состояние:")
        for org in self.organisms:
            status = "✅ жив" if org.is_alive() else "💀 мёртв"
            print(f"  {org.name}: энергия = {org.energy:.1f} ({status})")

# Главный модуль консольного симулятора жизни
# Запускает симуляцию экосистемы с хищниками и жертвами

from ecosystem import Ecosystem
from organism import Prey, Predator

url = "https://github.com/larinan13/life_simulator"
def main():
    # Создаём экосистему
    eco = Ecosystem(name="Лес")
    
    # Создаём организмы
    rabbit = Prey("Заяц", energy=50, escape_chance=0.6)
    deer = Prey("Олень", energy=80, escape_chance=0.3)
    wolf = Predator("Волк", energy=60, hunting_success=0.7)
    fox = Predator("Лиса", energy=40, hunting_success=0.5)
    
    # Добавляем в экосистему
    eco.add_organism(rabbit)
    eco.add_organism(deer)
    eco.add_organism(wolf)
    eco.add_organism(fox)
    
    # Симуляция нескольких дней
    print("=== НАЧАЛО СИМУЛЯЦИИ ===\n")
    for day in range(1, 6):
        print(f"\n--- День {day} ---")
        eco.simulate_day()
        eco.show_status()
        if not eco.has_alive_organisms():
            print("\nВсе организмы погибли. Симуляция завершена.")
            break
    
    print("\n=== КОНЕЦ СИМУЛЯЦИИ ===")

if __name__ == "__main__":
    main()

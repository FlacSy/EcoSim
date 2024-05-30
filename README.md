# EcoSim

EcoSim - это библиотека для проведения симуляций экосистем с учетом множества факторов.

## Установка

Установка производится через pip:

```bash
pip install ecosim
```

Для установки последней версии из репозитория:

```bash
pip install git+https://github.com/FlacSy/EcoSim
```

## Быстрый старт

### Импорт и использование библиотеки

```python
from ecosim import Climate, AnimalPopulation, PlantDistribution, Ecosystem, PredatorPreyPopulation, plot_simulation

def main():
    # Создание объектов, описывающих климат, популяцию животных, распределение растений и взаимодействие хищник-жертва
    climate = Climate(initial_temperature=15.0, temperature_variability=1.0, initial_precipitation=100.0, precipitation_variability=10.0)
    animal_population = AnimalPopulation(initial_population=100, birth_rate=0.1, death_rate=0.05, migration_rate=0.01)
    plant_distribution = PlantDistribution(initial_distribution=1000, spread_rate=50, competition_factor=0.01)
    predator_prey_population = PredatorPreyPopulation(prey_population=500, predator_population=50, prey_birth_rate=0.2, predator_birth_rate=0.1, predation_rate=0.01, predator_death_rate=0.05)

    # Создание экосистемы с учетом заданных параметров
    ecosystem = Ecosystem(climate, animal_population, plant_distribution, predator_prey_population)

    # Подготовка данных для симуляции
    data = {
        'Temperature': [],
        'Precipitation': [],
        'Animal Population': [],
        'Plant Distribution': [],
        'Prey Population': [],
        'Predator Population': []
    }

    # Симуляция на протяжении 50 лет
    for year in range(50):
        ecosystem.simulate_year()
        # Запись данных о состоянии экосистемы
        data['Temperature'].append(climate.temperature)
        data['Precipitation'].append(climate.precipitation)
        data['Animal Population'].append(animal_population.population)
        data['Plant Distribution'].append(plant_distribution.distribution)
        data['Prey Population'].append(predator_prey_population.prey_population)
        data['Predator Population'].append(predator_prey_population.predator_population)
    
    # Визуализация результатов симуляции
    plot_simulation(data, 'Ecosystem Simulation Over 50 Years').show()

if __name__ == '__main__':
    main()

```

## Лицензия

EcoSim распространяется под [MIT License](LICENSE). Подробности доступны в файле LICENSE.
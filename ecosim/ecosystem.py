class Ecosystem:
    def __init__(self, climate, animal_population, plant_distribution, predator_prey_population=None):
        self.climate = climate
        self.animal_population = animal_population
        self.plant_distribution = plant_distribution
        self.predator_prey_population = predator_prey_population

    def simulate_year(self):
        temperature, precipitation = self.climate.simulate_year()
        animal_population = self.animal_population.simulate_year()
        plant_distribution = self.plant_distribution.simulate_year()
        
        if self.predator_prey_population:
            prey_population, predator_population = self.predator_prey_population.simulate_year()
            print(f"Yearly update - Temperature: {temperature}, Precipitation: {precipitation}, Animal Population: {animal_population}, Plant Distribution: {plant_distribution}, Prey Population: {prey_population}, Predator Population: {predator_population}")
        else:
            print(f"Yearly update - Temperature: {temperature}, Precipitation: {precipitation}, Animal Population: {animal_population}, Plant Distribution: {plant_distribution}")

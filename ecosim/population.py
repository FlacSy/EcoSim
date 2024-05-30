class AnimalPopulation:
    def __init__(self, initial_population, birth_rate, death_rate, migration_rate=0.0):
        self.population = initial_population
        self.birth_rate = birth_rate
        self.death_rate = death_rate
        self.migration_rate = migration_rate

    def simulate_year(self):
        births = self.population * self.birth_rate
        deaths = self.population * self.death_rate
        migration = self.population * self.migration_rate
        self.population += births - deaths + migration
        return self.population

class PredatorPreyPopulation:
    def __init__(self, prey_population, predator_population, prey_birth_rate, predator_birth_rate, predation_rate, predator_death_rate):
        self.prey_population = prey_population
        self.predator_population = predator_population
        self.prey_birth_rate = prey_birth_rate
        self.predator_birth_rate = predator_birth_rate
        self.predation_rate = predation_rate
        self.predator_death_rate = predator_death_rate

    def simulate_year(self):
        prey_births = self.prey_population * self.prey_birth_rate
        predation = self.predation_rate * self.prey_population * self.predator_population
        predator_births = predation * self.predator_birth_rate
        predator_deaths = self.predator_population * self.predator_death_rate
        
        self.prey_population += prey_births - predation
        self.predator_population += predator_births - predator_deaths
        
        return self.prey_population, self.predator_population
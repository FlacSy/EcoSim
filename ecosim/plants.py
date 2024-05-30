class PlantDistribution:
    def __init__(self, initial_distribution, spread_rate, competition_factor):
        self.distribution = initial_distribution
        self.spread_rate = spread_rate
        self.competition_factor = competition_factor

    def simulate_year(self):
        self.distribution += self.spread_rate - (self.distribution * self.competition_factor)
        return self.distribution

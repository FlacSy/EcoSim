import numpy as np

class Climate:
    def __init__(self, initial_temperature, temperature_variability, initial_precipitation, precipitation_variability):
        self.temperature = initial_temperature
        self.temperature_variability = temperature_variability
        self.precipitation = initial_precipitation
        self.precipitation_variability = precipitation_variability

    def simulate_year(self):
        self.temperature += np.random.uniform(-self.temperature_variability, self.temperature_variability)
        self.precipitation += np.random.uniform(-self.precipitation_variability, self.precipitation_variability)
        return self.temperature, self.precipitation

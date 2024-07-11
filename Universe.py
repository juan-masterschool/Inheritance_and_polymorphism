from scipy import constants
from abc import ABC, abstractmethod


# Class for defining a CelestialBody
class CelestialBody(ABC):
    def __init__(self, name, radius_in_m, mass_in_kg, mean_temperature_in_celsius, age_in_years):
        self.name = name
        self.radius_in_m = radius_in_m
        self.mass_in_kg = mass_in_kg
        self.mean_temperature_in_celsius = mean_temperature_in_celsius
        self.age_in_years = age_in_years

    def gravitational_acceleration(self):
        return (constants.gravitational_constant * self.mass_in_kg) / (self.radius_in_m ** 2)

    # Abstract method that each subclass will have to implement
    @abstractmethod
    def get_host(self):
        pass


# Class for defining a Planet
class Planet(CelestialBody):
    def __init__(self, name, radius_in_m, mass_in_kg, mean_temperature_in_celsius, age_in_years, is_habitable,
                 host_star=None):
        super().__init__(name, radius_in_m, mass_in_kg, mean_temperature_in_celsius, age_in_years)
        self.is_habitable = is_habitable
        self.host_star = host_star

    def get_host(self):
        return self.host_star


# Class for defining a Star
class Star(CelestialBody):
    def __init__(self, name, radius_in_m, mass_in_kg, mean_temperature_in_celsius, age_in_years,
                 surrounding_planets=None, host_galaxy=None):
        super().__init__(name, radius_in_m, mass_in_kg, mean_temperature_in_celsius, age_in_years)
        self.surrounding_planets = surrounding_planets
        self.host_galaxy = host_galaxy

    def get_host(self):
        return self.host_galaxy


# Class for defining a Moon
class Moon(CelestialBody):
    def __init__(self, name, radius_in_m, mass_in_kg, mean_temperature_in_celsius, age_in_years, host_planet=None):
        super().__init__(name, radius_in_m, mass_in_kg, mean_temperature_in_celsius, age_in_years)
        self.host_planet = host_planet

    def get_host(self):
        return self.host_planet


from scipy import constants


# Class for defining a Planet
class Planet:
    def __init__(self, name, radius_in_m, mass_in_kg, mean_temperature_in_celsius, age_in_years, is_habitable, host_star=None):
        self.name = name
        self.radius_in_m = radius_in_m
        self.mass_in_kg = mass_in_kg
        self.mean_temperature_in_celsius = mean_temperature_in_celsius
        self.age_in_years = age_in_years
        self.is_habitable = is_habitable
        self.host_star = host_star

    # Method for calculating the gravitational acceleration
    # Notice how the method is the same in all classes
    def gravitational_acceleration(self):
        return (constants.gravitational_constant * self.mass_in_kg) / (self.radius_in_m ** 2)


# Class for defining a Star
class Star:
    def __init__(self, name, radius_in_m, mass_in_kg, mean_temperature_in_celsius, age_in_years, surrounding_planets=None):
        self.name = name
        self.radius_in_m = radius_in_m
        self.mass_in_kg = mass_in_kg
        self.mean_temperature_in_celsius = mean_temperature_in_celsius
        self.age_in_years = age_in_years
        self.surrounding_planets = surrounding_planets

    def gravitational_acceleration(self):
        return (constants.gravitational_constant * self.mass_in_kg) / (self.radius_in_m ** 2)


# Class for defining a Moon
class Moon:
    def __init__(self, name, radius_in_m, mass_in_kg, mean_temperature_in_celsius, age_in_years, host_planet=None):
        self.name = name
        self.radius_in_m = radius_in_m
        self.mass_in_kg = mass_in_kg
        self.mean_temperature_in_celsius = mean_temperature_in_celsius
        self.age_in_years = age_in_years
        self.host_planet = host_planet

    def gravitational_acceleration(self):
        return (constants.gravitational_constant * self.mass_in_kg) / (self.radius_in_m ** 2)

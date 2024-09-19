class City:
    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks


sancris = City('San Cristóbal de Las Casas', 'Mexico', 275000, ['Chamula', 'Nightlife', 'Weed smoking', 'Museums'])

tokyo = City('Tokyo', 'Japan', 14180000000, ['Meiji Jingu', 'Tokyo National Museum', 'Shibuya Crossing'])

print(vars(sancris))
print(vars(tokyo))
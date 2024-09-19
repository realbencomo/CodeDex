class Pokemon:
    def __init__(self, entry, name, types, description, is_caught, level, region, height, weight):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description  
        self.is_caught = is_caught
        self.level = level
        self.region = region
        self.height = height
        self.weight = weight

    def speak(self):
        print(f'{self.name}, {self.name}!')
        
    def display_details(self):
        print(f'Entry number: {self.entry}\n'
              f'Name: {self.name}\n'
              f'Types: {", ".join(self.types)}\n'  
              f'Description: {self.description}\n'
              f'Caught: {self.is_caught}\n'
              f'Level: {self.level}\n'
              f'Region: {self.region}\n'
              f'Height: {self.height} meters\n'
              f'Weight: {self.weight} kg')


bulbasaur = Pokemon(1, 'Bulbasaur', ['Grass', 'Poison'], 
                    'For some time after its birth, it uses the nutrients that are packed into the seed on its back in order to grow.', 
                    True, 5, 'Kanto', 0.7, 6.9)

charizard = Pokemon(6, 'Charizard', ['Fire', 'Flying'], 
                    'If Charizard becomes truly angered, the flame at the tip of its tail burns in a light blue shade.', 
                    True, 40, 'Kanto', 1.7, 90.5)

rayquaza = Pokemon(384, 'Rayquaza', ['Dragon', 'Flying'], 
                   'Rayquaza is said to have lived for hundreds of millions of years. Legends remain of how it put to rest the clash between Kyogre and Groudon.', 
                   False, 80, 'Hoenn', 7, 206.5)


rayquaza.speak()
rayquaza.display_details()

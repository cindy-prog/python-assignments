#index subclass 
class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def introduce(self):
        print(f"I am {self.name} from {self.universe} universe! and my power is {self.power}.")

    def fight_crime(self):
        print(f"{self.name} is fighting crime with {self.power}!")
    
    def move(self):
        print(f"{self.name} is now moving in mysterious ways.")
 #speedster subclass   
class Speedster(Superhero):
    def __init__(self, name, universe, speed):
        super().__init__(name, "Super Speed", universe)
        self.speed = speed
    
    def fight_crime(self):
        print(f"{self.name} is moving through the city at {self.speed} km/h in order to fight crime!")

    def move(self):
        print(f"{self.name} is running at a very fast speed!")
#flyer subclass
class Flyer(Superhero):
    def __init__(self, name, universe, altitude):
        super().__init__(name, "Flight", universe)
        self.altitude = altitude
        
    def fight_crime(self):
        print(f"{self.name} is flying in the sky at {self.altitude} meters!")

    def move(self):
        print(f"{self.name} is flying at a very fast speed!")
# swimmer subclass
class Swimmer(Superhero):
    def __init__(self, name, universe, swim_speed):
        super().__init__(name, "Breathing underwater", universe)
        self.swim_speed = swim_speed
     
    def fight_crime(self):
        print(f"{self.name} is swimming through the ocean at {self.swim_speed} knots!")

    def move(self):
        print(f"{self.name} is swimming with great joy!")
#create superhero objects
heroes = [
    Speedster("The_Flash", "Washington_DC", 6000),
    Flyer("Superwoman", "Atlanta", 7800),
    Swimmer("Rupanzel", "UK", 100)
]
# loop through all the heroes and show polymorphism
for hero in heroes:
    hero.introduce()
    hero.fight_crime()
    hero.move()
    print("-" * 40)
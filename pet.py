class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Default hunger level
        self.energy = 5  # Default energy level
        self.happiness = 5  # Default happiness level
        self.tricks = []  # List to store learned tricks

    def eat(self):
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)
        print(f"{self.name} ate some food.")

    def sleep(self):
        self.energy = min(self.energy + 5, 10)
        print(f"{self.name} had a nice rest.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger + 1, 10)
            print(f"{self.name} played and had fun!")
        else:
            print(f"{self.name} is too tired to play.")

    def get_status(self):
        print("\nPet Status Report:")
        print(f"Name      : {self.name}")
        print(f"Hunger    : {self.hunger}/10")
        print(f"Energy    : {self.energy}/10")
        print(f"Happiness : {self.happiness}/10")
        print("-" * 20)

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(self.happiness + 2, 10)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows {trick}.")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks:")
            for trick in self.tricks:
                print(f"{trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
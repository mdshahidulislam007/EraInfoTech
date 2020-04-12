class Animal:
    def __init__(self, name, height, weight, sound):
        self.name = name
        self.height = height
        self.weight = weight
        self.sound = sound

    def __str__(self):
        return "{} is {} cm tall and {} kilograms and say {}".format(self.name,
                                                                     self.height,
                                                                     self.weight,
                                                                     self.sound)

class Dog(Animal):
    def __init__(self, name, height, weight, sound, owner):
        super(Dog, self).__init__(name, height, weight, sound)
        self.owner = owner


    def __str__(self):
        s = super(Dog, self).__str__()
        return "{} His owner is {}".format(s, self.owner)

spot = Dog("Spot", 53, 27, "Ruff", "Derek")

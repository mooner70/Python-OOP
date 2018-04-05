class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        print self.name
    def walk(self):
        self.health = self.health + 1
        print self.health, "walk"
        return self
    def run(self):
        self.health = self.health + 5
        print self.health, "run"
        return self
    def display_health(self):
        print self.health
        return self

class Dog(Animal):
    def __init__(self):
        super(Animal, self).__init__()
        self.name = name
        self.health = 150
    def pet(self):
        self.health = self.health + 5
        return self

class Dragon(Animal):
    def __init__(self):
        super(Animal, self).__init__()
        self.health = 170
        print "I am a Dragon"
    def fly(self):
        self.health = self.health - 10



# animal=Dog("Meiko", 100)
dog=Dog()
# dragon=Dragon()
dog.name
dog.walk().walk().walk().run().run().pet()
dog.display_health()

# dragon.walk().walk().walk().run().run().fly()
# dragon.display_health()
    

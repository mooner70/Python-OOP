class Car(object):
    def __init__(self, price, speed, fuel, milage):
        self.price = price
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.speed = speed
        self.fuel = fuel
        self. milage = milage

    def displayAll(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel level:", self.fuel
        print "Milage:", self. milage
        print "Sales tax:", self.tax
        return self
    
car1=Car("$2,000", "35mph", "Full", "15mpg")
car2=Car("$2,000", "5mph", "Not Full", "105mpg")
car3=Car("$2,000", "15mph", "Kind of Full", "95mpg")
car4=Car("$2,000", "25mph", "Full", "25mpg")
car5=Car("$2,000", "45mph", "Empty", "25mpg")
car6=Car("$20,000,000", "35mph", "Empty", "15mpg")

car6.displayAll()

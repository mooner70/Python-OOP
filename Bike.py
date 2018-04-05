class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayinfo(self):
        print "${}".format(self.price)
        print self.max_speed
        if self.miles < 0:
            print "Miles are negative"
        else:
            print self.miles
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        return self

bike1=Bike(200, "100 MPH", 200)
bike2=Bike(500, "200 MPH", 150)
bike3=Bike(250, "130 MPH", 250)



print "BIKE #1:"
bike1.ride().ride().ride().reverse()
bike1.displayinfo()

print "BIKE #2"
bike2.ride().ride().reverse().reverse()
bike2.displayinfo()

print "BIKE #3"
bike3.reverse().reverse().reverse()
bike3.displayinfo()






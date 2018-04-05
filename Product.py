class Product(object):
    def __init__(self, price, item_name, weight, brand, status):
        self.price = price
        self.tax = .08
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"

    def sell(self):
        self.status = "Sold"
        return self
    def add_tax(self):
        self.price += (self.price * self.tax)
        return self
    def ret(self, reason):
        if reason == "Defective":
            self.price = 0
            self.status = reason
        if reason == "Like New":
            self.status = "For Sell"
        if reason == "Opened":
            self.status = "Used"
            self.price = self.price-(self.price * .2)
        return self
    def display(self):
        print "Price:", self.price
        print "Item:", self.item_name
        print self.weight, "lbs"
        print "Brand:", self.brand
        print "Status:", self.status
        return self

    
product1=Product(10, "shirt", 1, "Polo", "For Sale") 
product2=Product(15, "pants", 2, "Old Navy", "Defective")
product3=Product(3, "socks", 1, "Hanes", "For Sale")
product4=Product(50, "shoes", 2, "Nike", "For Sale")

# product2.add_tax().sell().display().ret("Like New").display()
product2.display()
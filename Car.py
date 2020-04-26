class Car:
    # properties
    color = ""
    brand = ""
    number_of_wheels = 4
    number_of_seats = 4
    maxspeed = 0

    # Conatructer
    def __init__(self, color, brand, number_of_wheels, number_of_seats, maxspeed):
        self.color = color
        self.brand = brand
        self.number_of_wheels = number_of_wheels
        self.number_of_seats = number_of_seats
        self.maxspeed = maxspeed

    # Cearte metthod
    def setcolor(self, x):
        self.color = x

    def setbrand(self, x):
        self.brand = x

    def setmaxspeed(self, x):
        self.maxspeed = x

    def printdata(self):
        print("Color of car is ", self.color)
        print("Brand of car is ", self.brand)
        print("Maxspeed of car is ", self.maxspeed)

    # DeConatructer

    def __del__(self):
        print()

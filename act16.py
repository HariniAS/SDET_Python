class car:
    'this is a sample'
    def __init__(self, manufacturer, model, make, transmission, color):
        self.manufacturer = manufacturer
        self.model = model
        self.make = make
        self.transmission = transmission
        self.color = color
    def accelerate(self):
        print (self.manufacturer, self.model, " is moving")
    def stop(self):
        print (self.manufacturer+ self.model+ " has stopped")

car1 = car("toyota","2020", "Q3", "F1", "Blue")
car2 = car("bmw","2019", "Q1", "F5", "Red")
car3 = car("audi","2018", "Q2", "F2", "Grey")
car1.accelerate()
car1.stop()
car2.accelerate()
car2.stop()
car3.accelerate()
car3.stop()
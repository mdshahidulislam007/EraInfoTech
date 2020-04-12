import copy
class Car:
    def __init__(self):
        self.engine = '2000cc'
        self.color = 'White'
        self.model = 'AUDI A5'
        self.seats = '5'
    def display(self):
        print(self.engine)
        print(self.color)
        print(self.model)
        print(self.seats)
        

car1 = Car()
car1.display()   
car2 = copy.deepcopy(car1)

car2.display()

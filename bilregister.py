class Car():
    
    def __init__(self, brand, color, mileage):
     
       self.brand = brand
       self.color = color
       self.mileage = mileage

    def brand(self):
     
       print(self.brand)

    def setbrand(self, new_brand):
     
       self.brand = new_brand

    def color(self, new_color):
        self.color = new_color

    def get_mileage(self):
        print(self.mileage)



a_car = Car('Volvo', 'Blå', 1587)
#a_car.get_brand()

b_car = Car('Wolwo', 'Röd', 1000)
#b_car.get_brand()

c_car = Car('Taxi', 'Gul', 3000)
#c_car.get_brand()

d_car = Car('Tesla','Grön', 4000)
#d_car.get_brand()

my_cars = [a_car, b_car, c_car, d_car]


for car in my_cars:
    print(car.brand, car.mileage, car.color)



    

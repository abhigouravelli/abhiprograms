class Vehicle:
    def wright_per_passenger(self):
        return self.weight/self.passengers
    def passenger_economy(self):
        return self.vehicle_economy * self.passenegers

my_car = Vehicle()
my_car.weight = 1500
my_car.passengers = 5
my_car.weight_per_passenger()
my_car.passenger_economy()
my_car.vehicle_economy = 20
my_car.passenger_economy()
my_747 = Vehicle()
my_747.vehicle_economy = 0.18
my_747.passengers = 500
my_747.passenger_economy()

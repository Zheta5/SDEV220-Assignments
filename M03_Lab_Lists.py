#Author: Carlos Guillen
#Date: 06/20/2024
#Purpose: Create a program that asks the user to input the type of vehicle they have, the year, make,model, number of doors, and type of roof.
class Vehicle(): 
    def __init__(self,vehicle_type):
        self.vehicle_type = vehicle_type
    
class Automobile(Vehicle):
    def __init__(self,vehicle_type,year,make,model,doors,roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

Vehicle_type = input("What type of vehicle is it, a car or truck? ")
vehicle=Vehicle(Vehicle_type)


year = int(input("What is the year of the vehicle? "))
make = input("What is the make of the vehicle? ")
model = input("What is the model of the vehicle? ")
doors = int(input("How many doors does the vehicle have? "))
roof = input("What type of roof does the vehicle have? ")
automobile = Automobile(Vehicle_type,year,make,model,doors,roof)


print("Vehicle Type:",automobile.vehicle_type)
print("Year:",automobile.year)
print("Make:",automobile.make)
print("Model:",automobile.model)
print("Doors:",automobile.doors)
print("Roof:",automobile.roof)





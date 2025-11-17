from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, base_fare, per_km, per_min):
        self.base_fare = base_fare
        self.per_km = per_km
        self.per_min = per_min

    @abstractmethod
    def calculate_fare(self, distance_km, duration_min):
        pass

class Bike(Vehicle):
    def calculate_fare(self, distance_km, duration_min):
        fare = self.base_fare + self.per_km * distance_km + self.per_min * duration_min
        return round(fare, 2)

class Auto(Vehicle):
    def calculate_fare(self, distance_km, duration_min):
        surge = 1.1 if distance_km < 2 else 1.0
        fare = (self.base_fare + self.per_km * distance_km + self.per_min * duration_min) * surge
        return round(fare, 2)

class Sedan(Vehicle):
    def calculate_fare(self, distance_km, duration_min):
        luggage_fee = 20 if distance_km > 10 else 0
        fare = self.base_fare + self.per_km * distance_km + self.per_min * duration_min + luggage_fee
        return round(fare, 2)

vehicles = {
    "bike": Bike(base_fare=20, per_km=6, per_min=0.5),
    "auto": Auto(base_fare=30, per_km=8, per_min=0.6),
    "sedan": Sedan(base_fare=50, per_km=12, per_min=1.0)
}

def fare_for_type(vtype, km, mins):
    v = vehicles[vtype]
    return v.calculate_fare(km, mins)

print(fare_for_type("bike", 5, 12))
print(fare_for_type("auto", 1.5, 8))
print(fare_for_type("sedan", 15, 25))

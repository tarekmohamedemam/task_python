class Car:
    def __init__(self, name, fuelRate=100, velocity=0):
        self.name = name
        self.fuelRate = min(max(fuelRate, 0), 100)
        self.velocity = min(max(velocity, 0), 200)

    def run(self, velocity, distance):
        if self.fuelRate <= 0:
            print("Can't start the car. Fuel is empty.")
            return
        self.velocity = min(max(velocity, 0), 200)
        fuel_needed = (distance / 10) * 10
        if fuel_needed >= self.fuelRate:
            distance_covered = (self.fuelRate / 10) * 10
            self.fuelRate = 0
            print(f"The car stopped after {distance_covered} km. Fuel finished.")
            self.stop(distance - distance_covered)
        else:
            self.fuelRate -= fuel_needed
            print(f"Car reached destination after {distance} km.")
            self.stop(0)

    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance > 0:
            print(f"Car stopped before destination. {remaining_distance} km remaining.")
        else:
            print("You have arrived at your destination.")

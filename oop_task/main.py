from car import Car
from person import Person
from employee import Employee
from office import Office
samy_car = Car(name="Fiat128", fuelRate=100, velocity=60)
samy = Employee(
    name="Samy",
    money=1000,
    mood="neutral",
    healthRate=80,
    id=1,
    car=samy_car,
    email="samy@iti.gov.eg",
    salary=5000,
    distanceToWork=20
)

iti_office = Office("ITI Smart Village")
iti_office.hire(samy)
samy.sleep(6)
print(f"Samy's mood after sleep: {samy.mood}")
samy.eat(2)
print(f"Samy's health after eating: {samy.healthRate}%")
samy.buy(3)
print(f"Samy's money after buying: {samy.money} L.E")
samy.drive()
iti_office.check_lateness(1, 7.5)
print(f"Samy's salary after lateness check: {samy.salary} L.E")


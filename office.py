from employee import Employee

class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, emp_id):
        emp = self.get_employee(emp_id)
        if emp:
            self.employees.remove(emp)
            Office.employeesNum -= 1

    def deduct(self, emp_id, deduction):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary -= deduction

    def reward(self, emp_id, reward):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += reward

    def check_lateness(self, emp_id, moveHour):
        emp = self.get_employee(emp_id)
        if emp:
            velocity = emp.car.velocity if emp.car.velocity > 0 else 80
            is_late = self.calculate_lateness(9, moveHour, emp.distanceToWork, velocity)
            if is_late:
                print("Employee is late! -10 from salary")
                self.deduct(emp_id, 10)
            else:
                print("Employee is on time! +10 to salary")
                self.reward(emp_id, 10)

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        if velocity == 0:
            return True
        arrival_time = moveHour + (distance / velocity)
        return arrival_time > targetHour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num

class Person:
    moods = ('happy', 'tired', 'lazy')

    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self, hours):
        if hours == 7:
            self.mood = self.moods[0]
        elif hours < 7:
            self.mood = self.moods[1]
        elif hours > 7:
            self.mood = self.moods[2]
        return self.mood

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50
        return self.healthRate

    def buy(self, items):
        self.money -= items * 10
        return self.money


class Employee(Person):
    def __init__(self, id, name, money, mood, healthRate, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary >= 1000:
            self._salary = salary
        else:
            raise ValueError("Salary must be 1000 or more")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if email.endswith(".com"):
            self._email = email
        else:
            raise ValueError("Invalid email")

    @property
    def healthRate(self):
        return self._healthRate

    @healthRate.setter
    def healthRate(self, healthRate):
        if 0 <= healthRate <= 100:
            self._healthRate = healthRate
        else:
            raise ValueError("healthRate must be between 0 to 100")

    def work(self, hours):
        if hours == 8:
            self.mood = self.moods[0]
        elif hours > 8:
            self.mood = self.moods[1]
        elif hours < 8:
            self.mood = self.moods[2]
        return self.mood




    def send_mail(self, to, subject, msg, receiver_name):
        email_file = open(f"{receiver_name}.txt", "w")
        email_file.write(f"To: {to}\n")
        email_file.write(f"Subject: {subject}\n")
        email_file.write(f"Message: {msg}\n")
        email_file.close()


class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    def run(self, velocity, distance):
        self.velocity = velocity
        self.fuelRate -= (distance / self.velocity)
        self.stop(distance)

    def stop(self, distance):
        self.velocity = 0
        if self.fuelRate > 0:
            print(f"Car stopped with {self.fuelRate}L of gas left, {distance}km remaining to destination")
        else:
            print("Car has arrived at destination")

    def drive(self, distance):
        self.car.run(self.car.velocity, distance)

    def refuel(self, gasAmount=100):
        self.car.fuelRate += gasAmount


class Office:
    employeesNum = 0

    def __init__(self, name, employees=[]):
        self.name = name
        self.employees = employees

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for employee in self.employees:
            if employee.id == empId:
                return employee
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        employee = self.get_employee(empId)
        if employee:
            self.employees.remove(employee)
            Office.employeesNum -= 1
            return True
        else:
            return False

    def deduct(self, empId, deduction):
        employee = self.get_employee(empId)
        if employee:
            employee.salary -= deduction
            return True
        else:
            return False

    def reward(self, empId, reward):
        employee = self.get_employee(empId)
        if employee:
            employee.salary += reward
            return True
        else:
            return False

    def check_lateness(self, empId, moveHour):
        employee = self.get_employee(empId)
        if employee:
            targetHour = 9
            isLate = self.calculate_lateness(targetHour, moveHour, employee.distanceToWork, employee.car.velocity)
            if isLate:
                self.deduct(empId, 10)
            else:
                self.reward(empId, 10)

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        time_needed = distance / velocity
        move_time = moveHour + time_needed
        if move_time > targetHour:
            return True
        else:
            return False

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num

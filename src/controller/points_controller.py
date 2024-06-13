from src.database import Database
from src.model.employee import Employee
from src.model.points import Points


class Controller:
    def __init__(self):
        self.database = Database()
        self.employees = []
        self.points = []

    def add_employee(self, cpf, name, email):
        employee = Employee(cpf, name, email)

        self.database.employee_collection.insert_one(employee)
        self.employees.append(employee)

    def update_employee_name(self, cpf, name):
        self.database.employee_collection.update_one({
            "cpf": cpf,
        }, {"$set": {"name": name}})

    def add_points(self, employee_id, amount):
        pass

    def remove_points(self, employee_id, amount):
        pass

    def get_employee_points(self, employee_id):
        pass


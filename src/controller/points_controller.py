import datetime

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

        self.database.employee_collection.insert_one(employee.to_json())
        self.employees.append(employee)

    def update_employee_name(self, cpf, name):
        self.database.employee_collection.update_one({
            "cpf": cpf,
        }, {"$set": {"name": name}})

    def add_points(self, employee_id):
        points = self.database.point_collection.find_one({
            "employee_id": employee_id
        })
        if points:
            new_point = Points(employee_id, start_date=datetime.datetime.now())
            self.database.point_collection.insert_one(new_point.to_json())
        else:
            self.database.point_collection.update_one({
                "employee_id": employee_id
            }, {"$set": {"end_date": datetime.datetime.now()}})

    def remove_points(self, employee_id, amount):
        pass

    def get_employee_points(self, employee_id):
        pass


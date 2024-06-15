import datetime

import pymongo

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
        point = self.database.point_collection.find_one({
            "employee_id": employee_id,
            "end_time": None
        }, sort=[('start_time', pymongo.DESCENDING)])

        if point is None:
            new_point = Points(employee_id, start_date=datetime.datetime.now())
            self.database.point_collection.insert_one(new_point.to_json())
        elif point["end_time"] is None:
            self.database.point_collection.update_one({
                '_id': point['_id']
            }, {"$set": {"end_time": datetime.datetime.now().timestamp()}})
        else:
            raise Exception("Some thing is not ok!")

    def remove_points(self, employee_id):
        self.database.point_collection.delete_many({
            'employee_id': employee_id
        })

    def get_employee_by_cpf(self, cpf):
        return self.database.employee_collection.find_one({
            'cpf': cpf
        })

    def get_employees_points(self):
        points = list(
            self.database.point_collection.find(sort=[('start_time', pymongo.DESCENDING)])
        )

        for point in points:
            point['start_time'] = datetime.datetime.fromtimestamp(point['start_time']).strftime('%A %d. %B %Y')
            if 'end_time' in point and point['end_time'] is not None:
                point['end_time'] = datetime.datetime.fromtimestamp(point['end_time']).strftime("%A %d. %B %Y")
        return points

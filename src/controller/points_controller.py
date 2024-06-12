from src.model.employee import Employee
from src.model.points import Points


class PointsController:
    def __init__(self):
        self.employees = []
        self.points = []

    def add_employee(self, cpf, name, email, phone, address, role, salary, admission_date):
        employee = Employee(cpf, name, email, phone, address, role, salary, admission_date)
        self.employees.append(employee)
        self.points.append(Points(employee_id=cpf))

    def update_employee_name(self, employee_id, name):
        for employee in self.employees:
            if employee.id == employee_id:
                employee.name = name

    def add_points(self, employee_id, amount):
        pass

    def remove_points(self, employee_id, amount):
        pass

    def get_employee_points(self, employee_id):
        pass


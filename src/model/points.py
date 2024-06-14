from uuid import uuid4


class Points:
    def __init__(self, employee_id, start_date=None, end_date=None):
        self.point_id = str(uuid4())
        self.employee_id = employee_id
        self.start_date = start_date
        self.end_date = end_date

    def to_json(self):
        return {
            "point_id": self.point_id,
            "employee_id": self.employee_id,
            "start_date": self.start_date,
            "end_date": self.end_date,
        }

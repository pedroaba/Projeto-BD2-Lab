import datetime
from uuid import uuid4


class Points:
    def __init__(self, employee_id, start_date: datetime.datetime = None, end_date: datetime.datetime = None):
        self.point_id = str(uuid4())
        self.employee_id = employee_id
        self.start_time = start_date
        self.end_time = end_date

    def to_json(self):
        return {
            "point_id": self.point_id,
            "employee_id": self.employee_id,
            "start_time": self._get_timestamp(self.start_time),
            "end_time": self._get_timestamp(self.end_time),
        }

    @staticmethod
    def _get_timestamp(date: datetime.datetime | None):
        return date.timestamp() if date is not None else None

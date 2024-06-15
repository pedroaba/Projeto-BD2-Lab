from pymongo.collection import Collection
from pymongo.database import Database as MongoDatabase
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class Database:
    def __init__(self):
        self.conn = MongoClient("mongodb+srv://pedro007augustobarbosa:RkwVhRcueEGsCtzU@projeto-bd-2.cdge0lk.mongodb.net/?retryWrites=true&w=majority&appName=projeto-bd-2")

        try:
            self.conn.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")

            self.database: MongoDatabase = self.conn.get_database("POINTER_MANAGER_CLI")
            self.employee_collection: Collection = self.database.get_collection("EMPLOYEE")
            self.point_collection: Collection = self.database.get_collection("POINT")
        except Exception as e:
            print(e)

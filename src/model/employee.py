class Employee:
    def __init__(self, cpf, name, email):
        self.cpf = cpf
        self.name = name
        self.email = email

    def to_json(self):
        return {
            "cpf": self.cpf,
            "name": self.name,
            "email": self.email,
        }

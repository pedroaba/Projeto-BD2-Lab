from src.controller.points_controller import Controller


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class PointerCLI(SimpleCLI):
    def __init__(self):
        self.controller = Controller()

        self.add_command('register_employee', self.register_employee)
        self.add_command('register_point', self.register_point)
        self.add_command('resume', self.resume)
        self.add_command('report_points', self.report_points)
        self.add_command('update_employee_info', self.update_employee_info)

        self.run()

    def register_employee(self):
        cpf = input("Entre com o CPF: ")
        email = input("Entre com o E-mail: ")
        name = input("Entre com o Nome: ")

        self.controller.add_employee(cpf, email, name)

    def register_point(self):
        pass

    def resume(self):
        pass

    def report_points(self):
        pass

    def update_employee_info(self):
        pass

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class Manager(Employee):

    def find_customer(self):
        pass

    def apply_orders(self):
        pass


class Support(Employee):

    def handel_calls(self):
        pass


class Creator:
    def __init__(self):
        self.employees = []
        self.employees_roles = {"manager": Manager, "support": Support}

    def get_team(self, managers=3, support=2):
        for i in range(managers):
            employee = self.hire_person(role='manager', name=i)
            self.employees.append(employee)
        for i in range(support):
            employee = self.hire_person(role='support', name=i)
            self.employees.append(employee)

    def hire_person(self, role: str, name) -> Manager or Support:
        return self.employees_roles.get(role)(name=name, role=role)


if __name__ == "__main__":
    creator = Creator()
    creator.get_team(managers=5, support=3)
    print(creator.employees)

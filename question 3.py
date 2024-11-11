class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated salary for {self.name} to {self.salary}")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} to {self.department_name} department")

    def calculate_total_salary_expenditure(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name} is: {total_salary}")

    def display_all_employees(self):
        print(f"Employees in {self.department_name} department:")
        for employee in self.employees:
            employee.display_details()


# Interactive part
department = Department("Software Development")
employee1 = Employee("Alice", "E001", 50000)
employee2 = Employee("Bob", "E002", 60000)

department.add_employee(employee1)
department.add_employee(employee2)

department.calculate_total_salary_expenditure()
department.display_all_employees()


# Calculate employee bonus
def bonus(salary, rate=0.1, *extras, **options):
    total_bonus = salary * rate + sum(extras)

    if "cap" in options:
        total_bonus = min(total_bonus, options["cap"])

    return total_bonus


# Check bonus calculation
print("Basic bonus:", bonus(50000))
print("Bonus with extras:", bonus(50000, 0.1, 1000, 500))
print("Bonus with cap:", bonus(50000, 0.1, 1000, cap=5500))

# Custom exception for invalid salary
class InvalidSalaryError(Exception):
    pass

# Employee class
class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")

        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"


# Manager inherits from Employee
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return f"{super().get_details()}, Team size: {self.team_size}"


# Handle invalid employee salary
try:
    employee = Employee("Test Employee", -500)
except InvalidSalaryError as error:
    print("Error:", error)
finally:
    print("Transaction finished")

# Employee data from the assessment
import csv
from pathlib import Path

file_path = Path(__file__).resolve().parent.parent / "data" / "employees.csv"

with open(file_path, "r", newline="") as file:
    employees = list(csv.DictReader(file))

# Convert salary values to numbers
for employee in employees:
    employee["salary"] = int(employee["salary"])

# Employees earning above 50000
high_earners = [
    employee["name"]
    for employee in employees
    if employee["salary"] > 50000
]
print("Above 50000:", high_earners)

# Add a 10% salary raise
raised_salaries = list(
map(lambda employee: round(employee["salary"] * 1.10, 2), employees)
)
print("Salaries after 10% raise:", raised_salaries)

# Find employees from Chennai
chennai_employees = list(
    filter(lambda employee: employee["city"] == "Chennai", employees)
)
chennai_names = [employee["name"] for employee in chennai_employees]
print("Chennai:", chennai_names)

# Skip zero salaries and stop after the first salary above 85000
for employee in employees:
    salary = employee["salary"]

    if salary == 0:
        continue

    print(employee["name"], "-", salary)

    if salary > 85000:
        break
employee = Employee("Arun", 30000)
manager = Manager("Divya", 75000, 5)

print(employee.get_details())
print("Annual salary:", employee.annual_salary())
print(manager.get_details())
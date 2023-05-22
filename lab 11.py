import math

class Shape(ABC):
    def __init__(self, sides):
        self.sides = sides
    
    
    def compute_area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height, side):
        super().__init__(3)  # Triangle always has 3 sides
        self.base = base
        self.height = height
        self.side = side
    
    def compute_area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(0)  # Circle has no sides
        self.radius = radius
    
    def compute_area(self):
        return math.pi * self.radius ** 2

# Driver program
triangle = Triangle(1,2,3)
circle = Circle(3)

print("Triangle area:", triangle.compute_area())
print("Circle area:", circle.compute_area())

class Employee:
    def __init__(self, emp_name, emp_id, salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.salary = salary

    def salary_status(self):
        if self.salary >= 10000:
            return "High"
        elif self.salary >= 5000:
            return "Medium"
        else:
            return "Low"

class BuildingManager(Employee):
    def __init__(self, emp_name, emp_id, salary):
        super().__init__(emp_name, emp_id, salary)

class ProcurementManager(Employee):
    def __init__(self, emp_name, emp_id, salary):
        super().__init__(emp_name, emp_id, salary)

class LogisticsManager(Employee):
    def __init__(self, emp_name, emp_id, salary):
        super().__init__(emp_name, emp_id, salary)

def main():
    # Create a list of employees
    employees = [
        BuildingManager("John Doe", 12345, 10000),
        ProcurementManager("Jane Doe", 54321, 12000),
        LogisticsManager("Mike Smith", 78901, 15000)
    ]

    # Display the information for each employee
    for employee in employees:
        print("Employee Name:", employee.emp_name)
        print("Employee ID:", employee.emp_id)
        print("Salary:", employee.salary)
        print("Salary Status:", employee.salary_status())

if __name__ == "__main__":
    main()
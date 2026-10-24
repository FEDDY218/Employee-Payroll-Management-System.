
# Parent class containing details shared by all employees
class Employee:
    def __init__(self, name, employee_id, basic_salary):
        self.name = name
        self.employee_id = employee_id
        self.basic_salary = basic_salary

    # Return the employee's basic information
    def display_details(self):
        return (
            f"Name: {self.name}, "
            f"ID: {self.employee_id}, "
            f"Basic Salary: KSh {self.basic_salary}"
        )

    # The default salary is the basic salary
    def calculate_salary(self):
        return self.basic_salary


# Manager inherits the common attributes and methods from Employee
class Manager(Employee):
    def __init__(self, name, employee_id, basic_salary, bonus):
        # Initialize the attributes inherited from Employee
        super().__init__(name, employee_id, basic_salary)
        self.bonus = bonus

    # Override the salary method to include the manager's bonus
    def calculate_salary(self):
        return self.basic_salary + self.bonus

    # Include the bonus when displaying manager details
    def display_details(self):
        return (
            f"{super().display_details()}, "
            f"Bonus: KSh {self.bonus}"
        )


# Developer inherits the common employee attributes
class Developer(Employee):
    def __init__(
        self, name, employee_id, basic_salary, programming_language
    ):
        # Reuse the parent class constructor
        super().__init__(name, employee_id, basic_salary)
        self.programming_language = programming_language

    # Add the developer's programming language to their details
    def display_details(self):
        return (
            f"{super().display_details()}, "
            f"Programming Language: {self.programming_language}"
        )


# Payroll manages salary calculations and payment status
class Payroll:
    def __init__(self, employee, month):
        self.employee = employee
        self.month = month
        self.payment_status = "Pending"

        # Private attribute for storing the payment reference
        self.__payment_reference = None

    # Use the employee's own salary calculation method
    def calculate_payment(self):
        return self.employee.calculate_salary()

    def process_payment(self):
        # Prevent the same payroll from being processed twice
        if self.payment_status == "Paid":
            return "Payment already processed"

        # Do not process zero or negative salaries
        elif self.calculate_payment() <= 0:
            return "Invalid salary"

        else:
            # Assign a simple reference for this exercise
            self.__payment_reference = "PAY001"
            self.payment_status = "Paid"
            return "Payment processed successfully"

    # Return the current payment status
    def get_payment_status(self):
        return self.payment_status

    # Display a summary of the employee's payroll
    def display_payroll(self):
        return (
            f"Employee: {self.employee.name}\n"
            f"Month: {self.month}\n"
            f"Salary: KSh {self.calculate_payment()}\n"
            f"Payment Status: {self.get_payment_status()}"
        )


# Create one manager and one developer
manager = Manager("Feddy", "EMP001", 80000, 15000)
developer = Developer("Mary", "EMP002", 60000, "Python")

# Create separate payroll records for October
payroll1 = Payroll(manager, "October")
payroll2 = Payroll(developer, "October")

# Display employee details
print(manager.display_details())
print(developer.display_details())

# Calculate and process the manager's salary
print(payroll1.calculate_payment())
print(payroll1.process_payment())
print(payroll1.process_payment())

# Process the developer's salary
print(payroll2.process_payment())

# Display the manager's payroll summary
print(payroll1.display_payroll())

import sys

class Employee:
    employees = {
        "LEO": [], "Analyst": [], "Security": [], "Clerk": [], "Misc": []
    }
    
    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.appointments = []
        Employee.employees[department].append(self)
    
    def add_appointment(self, guest_name, date, time):
        self.appointments.append({"guest_name": guest_name, "date": date, "time": time, "employee": self.name})
    
    def get_agenda(self):
        if not self.appointments:
            return ["No appointments"]
        return [f"Employee: {self.name} | Guest: {appt['guest_name']} | Date: {appt['date']} | Time: {appt['time']}" for appt in self.appointments]

# Create example employees with sample appointments
example_employees = {
    "LEO": ["John Doe"],
    "Analyst": ["Jane Smith"],
    "Security": ["Mark Johnson"],
    "Clerk": ["Emily Davis"],
    "Misc": ["Michael Brown"]
}

for dept, names in example_employees.items():
    for name in names:
        emp = Employee(name, dept)
        emp.add_appointment("Guest A", "2025-04-10", "10:00 AM")
        emp.add_appointment("Guest B", "2025-04-12", "02:00 PM")

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Guest")
        print("2. Employee")
        print("3. Quit")
        choice = input("Select an option: ")
        if choice == "1":
            guest_menu()
        elif choice == "2":
            employee_menu()
        elif choice == "3":
            sys.exit()
        else:
            print("Invalid choice. Try again.")

def guest_menu():
    while True:
        print("\nGuest Menu")
        print("1. Request an appointment")
        print("2. Back")
        choice = input("Select an option: ")
        if choice == "1":
            request_appointment()
        elif choice == "2":
            return
        else:
            print("Invalid choice. Try again.")

def employee_menu():
    while True:
        print("\nEmployee Menu")
        print("1. Get agenda")
        print("2. Add employee")
        print("3. Back")
        print("4. Quit")
        choice = input("Select an option: ")
        if choice == "1":
            get_agenda()
        elif choice == "2":
            add_employee()
        elif choice == "3":
            return
        elif choice == "4":
            sys.exit()
        else:
            print("Invalid choice. Try again.")

def get_agenda():
    department = select_department()
    if department:
        employee = select_employee(department)
        if employee:
            print(f"\nAgenda for {employee.name}:")
            for appt in employee.get_agenda():
                print(appt)

def add_employee():
    name = input("Enter employee name: ")
    department = select_department()
    if department:
        Employee(name, department)
        print(f"Employee {name} added to {department}.")

def request_appointment():
    department = select_department()
    if department:
        employee = select_employee(department)
        if employee:
            guest_name = input("Enter your name: ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            employee.add_appointment(guest_name, date, time)
            print(f"Appointment scheduled with {employee.name} on {date} at {time}.")

def select_department():
    print("\nSelect a department:")
    for idx, dept in enumerate(Employee.employees.keys(), start=1):
        print(f"{idx}. {dept}")
    choice = input("Enter the number of the department: ")
    try:
        return list(Employee.employees.keys())[int(choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        return None

def select_employee(department):
    employees = Employee.employees.get(department, [])
    if not employees:
        print("No employees found in this department.")
        return None
    print("\nSelect an employee:")
    for idx, emp in enumerate(employees, start=1):
        print(f"{idx}. {emp.name}")
    choice = input("Enter the number of the employee: ")
    try:
        return employees[int(choice) - 1]
    except (IndexError, ValueError):
        print("Invalid choice.")
        return None

if __name__ == "__main__":
    main_menu()

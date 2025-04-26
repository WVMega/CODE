import tkinter as tk
from tkinter import messagebox
import csv
import sys
import os

# --- Data Classes ---
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.appointments = []

    def addAppointment(self, guest_name, date, time):
        self.appointments.append((guest_name, date, time))
        self.saveIt(guest_name, date, time)

    def saveIt(self, guest_name, date, time):
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))

        file_path = os.path.join(base_path, 'appointments.csv')

        write_header = not os.path.isfile(file_path)

        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            if write_header:
                writer.writerow(['Employee Name', 'Department', 'Guest Name', 'Date', 'Time'])
            writer.writerow([self.name, self.department, guest_name, date, time])

    def loadAppointments(self):
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))

        file_path = os.path.join(base_path, 'appointments.csv')
        if not os.path.isfile(file_path):
            return

        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Employee Name'] == self.name and row['Department'] == self.department:
                    self.appointments.append((row['Guest Name'], row['Date'], row['Time']))

departments = ['LEO', 'Analyst', 'Security', 'Clerk', 'Misc']
employees = {
    'LEO': [Employee("Fierce Strongrock", "LEO")],
    'Analyst': [Employee("Inge Weber", "Analyst")],
    'Security': [Employee("Robert Cunningham", "Misc")],
    'Clerk': [Employee("Echo Scott", "Clerk")],
    'Misc': [Employee("Pablo Vanco", "Misc")]
}

for deptEmps in employees.values():
    for emp in deptEmps:
        emp.loadAppointments()

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Walmart Calendly")
        self.root.geometry("500x500")
        self.mainMenu()

    def endIt(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mainMenu(self):
        self.endIt()
        tk.Label(self.root, text="Main Menu", font=("Arial", 16)).pack(pady=30)

        myButton = tk.Frame(self.root)
        myButton.pack()

        tk.Button(myButton, text="Guest", width=20, command=self.guestMenu).pack(pady=10)
        tk.Button(myButton, text="Employee", width=20, command=self.employeeMenu).pack(pady=10)
        tk.Button(myButton, text="Quit", width=20, command=self.root.quit).pack(pady=10)

    def guestMenu(self):
        self.endIt()
        tk.Label(self.root, text="Guest Menu", font=("Arial", 16)).pack(pady=30)

        myButton = tk.Frame(self.root)
        myButton.pack()

        tk.Button(myButton, text="Request Appointment", width=25, command=self.selectDepartment).pack(pady=10)
        tk.Button(myButton, text="Back", width=25, command=self.mainMenu).pack(pady=10)
        tk.Button(myButton, text="Quit", width=20, command=self.root.quit).pack(pady=10)

    def employeeMenu(self):
        self.endIt()
        tk.Label(self.root, text="Employee Menu", font=("Arial", 16)).pack(pady=30)

        myButton = tk.Frame(self.root)
        myButton.pack()

        tk.Button(myButton, text="Get Agenda", width=25, command=self.selectDepAdgenda).pack(pady=10)
        tk.Button(myButton, text="Add Employee", width=25, command=self.addEmployee).pack(pady=10)
        tk.Button(myButton, text="Back", width=25, command=self.mainMenu).pack(pady=10)
        tk.Button(myButton, text="Quit", width=25, command=self.root.quit).pack(pady=10)

    def selectDepartment(self):
        self.endIt()
        tk.Label(self.root, text="Select Department", font=("Arial", 16)).pack(pady=20)

        myButton = tk.Frame(self.root)
        myButton.pack()

        for i, dept in enumerate(departments):
            tk.Button(myButton, text=dept, width=20, command=lambda d=dept: self.selectEmp(d)).pack(pady=5)

        tk.Button(myButton, text="Back", width=20, command=self.guestMenu).pack(pady=10)

    def selectEmp(self, dept):
        self.endIt()
        tk.Label(self.root, text=f"Select Employee in {dept}", font=("Arial", 16)).pack(pady=20)

        myButton = tk.Frame(self.root)
        myButton.pack()

        for i, emp in enumerate(employees.get(dept, [])):
            tk.Button(myButton, text=emp.name, width=25, command=lambda e=emp: self.requestAppointment(e)).pack(pady=5)

        tk.Button(myButton, text="Back", width=20, command=self.selectDepartment).pack(pady=10)

    def requestAppointment(self, employee):
        self.endIt()
        tk.Label(self.root, text=f"Request Appointment with {employee.name}", font=("Arial", 16)).pack(pady=20)

        tk.Label(self.root, text="Enter your name:").pack(pady=5)
        guest_name_entry = tk.Entry(self.root, width=30)
        guest_name_entry.pack(pady=5)

        tk.Label(self.root, text="Enter the date (MM-DD-YYYY):").pack(pady=5)
        date_entry = tk.Entry(self.root, width=30)
        date_entry.pack(pady=5)

        tk.Label(self.root, text="Enter the time (HH:MM):").pack(pady=5)
        timeInput = tk.Entry(self.root, width=30)
        timeInput.pack(pady=5)

        def saveAppointment():
            guest_name = guest_name_entry.get()
            date = date_entry.get()
            time = timeInput.get()
            if guest_name and date and time:
                employee.addAppointment(guest_name, date, time)
                messagebox.showinfo("Appointment Saved", f"Appointment scheduled with {employee.name}.")
                self.guestMenu()

        myButton = tk.Frame(self.root)
        myButton.pack()

        tk.Button(myButton, text="Save Appointment", command=saveAppointment).pack(pady=10)
        tk.Button(myButton, text="Back", width=20, command=self.guestMenu).pack(pady=10)

    def selectDepAdgenda(self):
        self.endIt()
        tk.Label(self.root, text="Select Department", font=("Arial", 16)).pack(pady=20)

        myButton = tk.Frame(self.root)
        myButton.pack()

        for i, dept in enumerate(departments):
            tk.Button(myButton, text=dept, width=20, command=lambda d=dept: self.selectEmpAgenda(d)).pack(pady=5)

        tk.Button(myButton, text="Back", width=20, command=self.employeeMenu).pack(pady=10)

    def selectEmpAgenda(self, dept):
        self.endIt()
        tk.Label(self.root, text=f"Select Employee in {dept}", font=("Arial", 16)).pack(pady=20)

        myButton = tk.Frame(self.root)
        myButton.pack()

        for i, emp in enumerate(employees.get(dept, [])):
            tk.Button(myButton, text=emp.name, width=25, command=lambda e=emp: self.GetAgenda(e)).pack(pady=5)

        tk.Button(myButton, text="Back", width=20, command=self.selectDepAdgenda).pack(pady=10)

    def GetAgenda(self, employee):
        self.endIt()
        tk.Label(self.root, text=f"{employee.name}'s Appointments", font=("Arial", 16)).pack(pady=20)

        if employee.appointments:
            for i, (guest, date, time) in enumerate(employee.appointments):
                tk.Label(self.root, text=f"{date} at {time} - Guest: {guest}").pack(pady=2)
        else:
            tk.Label(self.root, text="No appointments.").pack(pady=10)

        myButton = tk.Frame(self.root)
        myButton.pack()

        tk.Button(myButton, text="Back", width=20, command=self.selectDepAdgenda).pack(pady=20)
        tk.Button(myButton, text="Quit", width=20, command=self.root.quit).pack(pady=20)

    def addEmployee(self):
        self.endIt()
        tk.Label(self.root, text="Add Employee", font=("Arial", 16)).pack(pady=20)

        tk.Label(self.root, text="Employee Name:").pack(pady=5)
        nameInput = tk.Entry(self.root, width=30)
        nameInput.pack(pady=5)

        tk.Label(self.root, text="Department:").pack(pady=5)
        deptInput = tk.Entry(self.root, width=30)
        deptInput.pack(pady=5)

        def saveEmployee():
            name = nameInput.get()
            dept = deptInput.get()
            if name and dept in departments:
                newEmp = Employee(name, dept)
                employees[dept].append(newEmp)
                messagebox.showinfo("Employee Added", f"{name} added to {dept}.")
                self.employeeMenu()

        myButton = tk.Frame(self.root)
        myButton.pack()

        tk.Button(myButton, text="Save Employee", command=saveEmployee).pack(pady=10)
        tk.Button(myButton, text="Back", width=20, command=self.employeeMenu).pack(pady=10)

# --- Run the App ---
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    app = MyApp(root)
    root.mainloop()

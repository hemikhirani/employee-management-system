import csv
import os

FILENAME = 'employee 1.csv'
ATTENDANCE_FILENAME = 'employee_attendance.csv'

def initialize_csv():
    """Initialize the CSV file with headers if it doesn't exist."""
    if not os.path.isfile(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Employee ID', 'Gender', 'Name', 'Age', 'Village', 'City', 'Phone Number', 'Position', 'Salary'])

def initialize_attendance_csv():
    """Initialize the attendance CSV file with headers if it doesn't exist."""
    if not os.path.isfile(ATTENDANCE_FILENAME):
        with open(ATTENDANCE_FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Employee ID', 'Date', 'Status'])

def get_phone_number():
    """Prompt for a phone number and validate it."""
    while True:
        phone_number = input("Enter Employee Phone Number (10 digits): ")
        if len(phone_number) == 10 and phone_number.isdigit():
            return phone_number
        else:
            print("Invalid phone number. Please enter exactly 10 digits.")

def get_gender():
    """Prompt for gender and validate it."""
    while True:
        gender = input("Enter Employee Gender (Male/Female/Other): ").strip().capitalize()
        if gender in ['Male', 'Female', 'Other']:
            return gender
        else:
            print("Invalid input. Please enter 'Male', 'Female', or 'Other'.")

def get_age():
    """Prompt for age and validate it."""
    while True:
        age = input("Enter Employee Age: ")
        if age.isdigit() and int(age) > 0:
            return age
        else:
            print("Invalid input. Please enter a valid age (positive number).")

def add_employee():
    """Add a new employee to the payroll."""
    employee_id = input("Enter Employee ID: ")
    gender = get_gender()
    name = input("Enter Employee Name: ")
    age = get_age()  
    village = input("Enter Village: ")
    city = input("Enter City: ")
    phone_number = get_phone_number()  
    position = input("Enter Employee Position: ")
    salary = input("Enter Employee Salary: ")

    try:
        with open(FILENAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([employee_id, gender, name, age, village, city, phone_number, position, salary])
        print("Employee added successfully.")
    except Exception as e:
        print(f"Error adding employee: {e}")

def view_employees():
    """View all employees ."""
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            employees = list(reader)  

        
            print(f"{header[0]:<15} {header[1]:<10} {header[2]:<20} {header[3]:<5} {header[4]:<15} {header[5]:<15} {header[6]:<15} {header[7]:<15} {header[8]:<10}")
            for row in employees:
                print(f"{row[0]:<15} {row[1]:<10} {row[2]:<20} {row[3]:<5} {row[4]:<15} {row[5]:<15} {row[6]:<15} {row[7]:<15} {row[8]:<10}")

    except Exception as e:
        print(f"Error viewing employees: {e}")

def update_employee():
    """Update an existing employee's information."""
    employee_id = input("Enter Employee ID to update: ")
    updated_rows = []
    found = False

    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            updated_rows.append(header)  

            for row in reader:
                if row[0] == employee_id:
                    found = True
                    print(f"Updating details for Employee ID: {employee_id}")
                    gender = get_gender()  
                    name = input("Enter new Employee Name: ")
                    age = get_age()  
                    village = input("Enter new Village: ")
                    city = input("Enter new City: ")
                    phone_number = get_phone_number()  
                    position = input("Enter new Employee Position: ")
                    salary = input("Enter new Employee Salary: ")
                    updated_rows.append([employee_id, gender, name, age, village, city, phone_number, position, salary])
                    print("Employee updated successfully.")
                else:
                    updated_rows.append(row)

        if not found:
            print("Employee ID not found.")

        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)

    except Exception as e:
        print(f"Error updating employee: {e}")

def delete_employee():
    """Delete an employee from the payroll."""
    employee_id = input("Enter Employee ID to delete: ")
    updated_rows = []
    found = False

    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            updated_rows.append(header)  

            for row in reader:
                if row[0] == employee_id:
                    found = True
                    print(f"Employee found: {row[2]} (ID: {row[0]})")  
                    confirm = input("Are you sure you want to delete this employee? (yes/no): ")
                    if confirm.lower() == 'yes':
                        print("Employee deleted successfully.")
                        continue  
                updated_rows.append(row)  

        if not found:
            print("Employee ID not found.")

        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)

    except Exception as e:
        print(f"Error deleting employee: {e}")

def mark_attendance():
    """Update attendance status for an employee."""
    employee_id = input("Enter Employee ID to mark attendance: ")
    status = input("Enter attendance status (Present/Absent): ").strip().capitalize()
    date = input("Enter the date (YYYY-MM-DD): ")

    if status not in ['Present', 'Absent']:
        print("Invalid status. Please enter 'Present' or 'Absent'.")
        return

    updated = False
    records = []

    if os.path.isfile(ATTENDANCE_FILENAME):
        with open(ATTENDANCE_FILENAME, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)  

            for row in reader:
                if row[0] == employee_id and row[1] == date:
                    if row[2] == status:
                        print("Attendance already marked as", status)
                        return
                    else:
                        row[2] = status  
                    updated = True
                records.append(row)

    if not updated:
        records.append([employee_id, date, status])
        print("New attendance record added.")
    else:
        print("Attendance status updated successfully.")

    with open(ATTENDANCE_FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)  
        writer.writerows(records)  

def view_attendance():
    """View attendance records."""
    try:
        with open(ATTENDANCE_FILENAME, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                print(f"Employee ID: {row[0]}, Date: {row[1]}, Status: {row[2]}")
    except Exception as e:
        print(f"Error viewing attendance: {e}")

def delete_attendance():
    """Delete an attendance record."""
    employee_id = input("Enter Employee ID to delete attendance: ")
    date = input("Enter the date (YYYY-MM-DD) of the attendance record to delete: ")
    updated_rows = []
    found = False

    try:
        with open(ATTENDANCE_FILENAME, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)  
            updated_rows.append(headers)  

            for row in reader:
                if row[0] == employee_id and row[1] == date:
                    found = True
                    print("Attendance record deleted successfully.")
                else:
                    updated_rows.append(row)

        if not found:
            print("Attendance record not found.")

        with open(ATTENDANCE_FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)

    except Exception as e:
        print(f"Error deleting attendance: {e}")

def main_menu():
    """Display the main menu and handle user input."""
    initialize_csv()
    initialize_attendance_csv()
    
    while True:
        print("\nEmployee Payroll System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Mark Attendance")
        print("6. View Attendance")
        print("7. Delete Attendance")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            mark_attendance()
        elif choice == '6':
            view_attendance()
        elif choice == '7':
            delete_attendance()
        elif choice == '8':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

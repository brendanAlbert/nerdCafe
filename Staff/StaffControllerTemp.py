from Staff import Staff
import os
import csv


def main():
    # TODO keep these member variables somehow

    is_running_staff_controller = True
    staff_file = "staff/staff.csv"
    fieldnames = ["Name", "ID", "Wage Rate", "Date Hired", "Hours Worked", "Overtime Hours", "Sick Days",
                  "Is Manager?"]

    if not os.path.exists("staff\\"):
        os.makedirs("staff\\")
    if not os.path.exists(staff_file):
        with open(staff_file, 'w', newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
    while is_running_staff_controller:
        choice = input("What would you like to do? (type a number)"
                       "\n1. View employees"
                       "\n2. Add a new employee (add them to database)"
                       "\n3. Fire an employee (delete them from database)"
                       "\n4. Modify information about an employee"
                       "\n0. Return to main menu")
        if choice == "1":
            print("\nHere is a list of all the employees who work here:")
            with open(staff_file, "r", newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    print(row["Name"])
                print()

        elif choice == "2":
            name = input("Enter the name of the new employee:")
            id = input("Enter an ID number for the new employee:")
            wage_rate = input("Enter the wage rate for the new employee:")
            new_employee = Staff(name, id, wage_rate)
            with open(staff_file, 'a', newline="") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)

        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "0":
            pass
            # TODO: Return back to main menu
        else:
            print("That is not a valid choice. Please try again.")


main()


import csv

try:
    n = int(input("Enter number of employees: "))

    with open("payroll.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow([
            "Employee ID", "Name", "Basic Salary",
            "Allowance", "Deduction", "Net Salary"
        ])

        # Accept employee details
        for i in range(n):
            print("\nEnter details of Employee", i + 1)

            emp_id = input("Employee ID: ")
            name = input("Name: ")
            basic = float(input("Basic Salary: "))
            allowance = float(input("Allowance: "))
            deduction = float(input("Deduction: "))

            net_salary = basic + allowance - deduction

            writer.writerow([
                emp_id, name, basic,
                allowance, deduction, net_salary
            ])

    print("\nPayroll records saved successfully!")

    # Read and display payroll records
    print("\n----- EMPLOYEE PAYROLL DETAILS -----")

    with open("payroll.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(" | ".join(row))

except ValueError:
    print("Please enter valid numeric values.")
except Exception as e:
    print("Error:", e)
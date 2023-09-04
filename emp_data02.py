emp_data = [
    {"emp ID": "161E90", "Name": "Raman", "Age": 41, "Salary": 56000},
    {"emp ID": "161F91", "Name": "Himadri", "Age": 38, "Salary": 67500},
    {"emp ID": "161F99", "Name": "Jaya", "Age": 51, "Salary": 82100},
    {"emp ID": "171E20", "Name": "Tejas", "Age": 30, "Salary": 55000},
    {"emp ID": "171G30", "Name": "Ajay", "Age": 45, "Salary": 44000},
]




def sort_emp_data(choice):
    if choice == 1:  
        sorted_data = sorted(emp_data, key=lambda x: x["Age"])
    elif choice == 2:  
        sorted_data = sorted(emp_data, key=lambda x: x["Name"])
    elif choice == 3:  
        sorted_data = sorted(emp_data, key=lambda x: x["Salary"])
    else:
        print("Invalid choice. Please select a valid sorting parameter (1, 2, or 3).")
        return

#----
#---
    print("\nSorted emp Data:")
    print("emp ID\tName\tAge\tSalary")
    for employee in sorted_data:
        print(
            f"{employee['emp ID']}\t{employee['Name']}\t{employee['Age']}\t{employee['Salary']}"
        )

print("Sort emp Data:")
print("1. Sort by Age")
print("2. Sort by Name")
print("3. Sort by Salary")
choice = int(input("Enter your choice (1/2/3): "))

sort_emp_data(choice)
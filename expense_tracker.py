import csv

expenses = []

try:
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            expenses.append({"Name": row[0], "Amount": float(row[1])})
except FileNotFoundError:
    pass

while True:
    print("\n--- Menu ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Delete Expense")
    print("5. Exit Application")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter the Expense name: ")
        amount = float(input("Enter expense amount: "))
        expenses.append({"Name":name, "Amount":amount})
        with open("expenses.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, amount])
        print("Expense added successfully!")

    elif choice == '2':
        print("\nYour Expenses:")
        for item in expenses:
            print(f"- {item['Name']}: ₹{item['Amount']}")
            
    elif choice == '3':
        total = 0
        for item in expenses:
            item['Amount']
            total = total + item['Amount']
        print(f'Total = {total}')
    
    elif choice == '4':
     if not expenses:
        print("No expenses to delete!")
     else:
        for i, item in enumerate(expenses):
            print(f"{i+1}. {item['Name']} - ₹{item['Amount']}")
        exp_num = int(input("Enter expense number to delete: "))
        index = exp_num - 1
        expenses.pop(index)
        with open("expenses.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for item in expenses:
                writer.writerow([item['Name'], item['Amount']])
        print("Expense deleted!")
    
    elif choice == '5':
        print("\n Exiting....")
        break
    
    else:
        print("Invalid Choice")

    
  
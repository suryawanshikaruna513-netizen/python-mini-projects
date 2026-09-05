# Expense Tracker

expenses = []

print("===== EXPENSE TRACKER =====")

while True:
    category = input("\nEnter expense category (or type 'done'): ")

    if category.lower() == "done":
        break

    amount = float(input("Enter amount: "))

    expenses.append({
        "category": category,
        "amount": amount
    })

print("\n===== EXPENSE SUMMARY =====")

total = 0

for expense in expenses:
    print(expense["category"], ":", expense["amount"])
    total += expense["amount"]

print("--------------------------")
print("Total Expense:", total)

if expenses:
    highest = max(expenses, key=lambda x: x["amount"])

    print("Highest Expense:")
    print(highest["category"], ":", highest["amount"])
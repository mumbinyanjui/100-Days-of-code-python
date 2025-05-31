# Day 2 - Tip Calculator (Mini Project)

print("Welcome to the tip calculator!")

# Taking input from user
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Tip and total calculations
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

# Round to 2 decimal places
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")

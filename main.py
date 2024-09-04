# Tip Calculator

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? "))
tip_percent = float(input("How much tip would you like to give? "))
no_of_people = float(input("How many people to split the bill? "))

per_person_pay = (total_bill + (total_bill * tip_percent / 100)) / no_of_people
rounded_per_person_pay = round(per_person_pay, 2)

print(f"Each person should pay: ${rounded_per_person_pay}")

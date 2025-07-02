# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Enter Kilograms or Pounds? (K or L):")

if unit == "K":
    weight = weight * 2.205
    print(f"Your weight is {round(weight, 2)}Lbs")
elif unit == "L":
    weight = weight / 2.205
    print(f"Your weight is {round(weight, 2)}Kg")
else:
    print(f"You did put the wrong unit {unit} please you use only (L/K). ")

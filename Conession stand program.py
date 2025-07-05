# Conession stand program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0
print("---------------Menu---------------")
for food, price in menu.items():
    print(f"- {food}: {price}$")
print("----------------------------------")

while True:
    food = input("Enter The item you want (Type 'done') if you finish: ").lower()
    if food == "done":
        break
    elif menu.get is not None:
        cart.append(food)

print("----------------------------------")
for food in cart:
    total += menu.get(food)
    print(food.capitalize(), end = " ")

print()
print(f"Your total is {total}$")
print("----------------------------------")
# Shopping Cart program

foods = []
prices = []
total = 0

while True:
   food = input("Enter a food to buy (q to quit): ")
   if food == "q":
      break
   else:
      price = float(input(f"Enter the price of the {food}: $"))
      foods.append(food)
      prices.append(price)

print()

print("--------------------------------- Your Cart ---------------------------------")

for food in foods:
   print(f"- {food}")

for price in prices:
   total += price

print(f"Your total is: {total}$")

print("-----------------------------------------------------------------------------")
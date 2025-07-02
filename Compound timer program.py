# Pyhton compound interset calcultor

principles = 0
rate = 0 
time = 0

while principles <= 0:
    principles = int(input("Enter the principle: "))
    if principles <= 0:
        print("Principles can't be less then zero !!!")

while rate <= 0:
    rate = int(input("Enter the rate: "))
    if rate <= 0:
        print("Rate can't be less then zero !!!")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be negative or zero !!!")

total = principles * pow((1 + rate / 100), time)

print(f'The final amount that you would get is: {total}$')
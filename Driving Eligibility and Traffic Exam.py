# Traffic Exam

User = input("Enter your name: ").lower()
print("Hello, " + User + "! Welcome to the program.")
print()
age = input("how old are you ?: ")

if int(age) >= 18:
    print("You are an adult now! you can pass the exam")
else :
    print(f'You are not an adult yet! you need to wait for a few years cause you are only {age} years old.')

print()

first_question = input('What does a red traffic light mean?: ')

if first_question == 'stop':
    print('Correct answer!')
else:
    print('Incorrect answer! The correct answer is "stop".')

print()

second_question = input('what should you do if you see a stop sign?: ')

if second_question == 'come to a complete stop, then proceed when safe':
    print('Correct answer!')
else:
    print('Incorrect answer! The correct answer is "Come to a complete stop, then proceed when safe".')

print()

third_question = input('When is it legal to use a mobile phone while driving?: ')

if third_question == 'when using a hands-free device':
    print('Correct answer!')
else:
    print('Incorrect answer! The correct answer is "When using a hands-free device".')

print()

if first_question == 'stop' and second_question == 'come to a complete stop, then proceed when safe' and third_question == 'when using a hands-free device':
    print(f'Congratulations! {User} You have passed the exam and now you have your driver license.') 
    print()
    print("Be careful on the road !!!")         
else:
    print(f'Sorry {User}, you have not passed the exam. Please try again later.')

# To check if the user can pass the exam, and if the user have successfully passed the exam and got there driver license.
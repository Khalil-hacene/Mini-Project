User = input("enter your name:").lower().strip()
print("Hello, " + User + "! Welcome to the program.")

age = input("how old are you ?:")
if int(age) >= 18:
    print("you are an adult now! you can pass the exam")
else :
    print(f'you are not an adult yet! you need to wait for a few years cause you are only {age} years old.')

if int(age) >= 18:
    print('You can start the exam now!')
first_question = input('What does a red traffic light mean?')

if first_question == 'stop':
    print('Correct answer!')
else:
    print('Incorrect answer! The correct answer is "stop".')

second_question = input('what should you do if you see a stop sign?')
if second_question == 'come to a complete stop, then proceed when safe':
    print('Correct answer!')
else:
    print('Incorrect answer! The correct answer is "Come to a complete stop, then proceed when safe".')

third_question = input('When is it legal to use a mobile phone while driving?')
if third_question == 'when using a hands-free device':
    print('Correct answer!')
else:
    print('Incorrect answer! The correct answer is "When using a hands-free device".')

if first_question == 'stop' and second_question == 'come to a complete stop, then proceed when safe' and third_question == 'when using a hands-free device':
    print(f'Congratulations! {User} You have passed the exam and now you have your driver license.')          
else:
    print(f'Sorry {User}, you have not passed the exam. Please try again later.')


# to check if the user can pass the exan, and if the user have successfully passed the exam and got the driver license.
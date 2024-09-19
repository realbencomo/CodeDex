print("BMI Calculator")

while True:
    mass = float(input("How much do you weigh in kilograms? "))
    height = float(input("How tall are you? In meters: "))
    bmi = mass / height**2
    print("Your BMI is:", bmi, "!")
    repLoop = input("Try again? Y/N: ").upper()
    if repLoop == "Y":
        continue
    else: 
        print("Thanks for using the BMI calculator!")
        break

import random

grade = random.randint(0, 101)

print ("Random test score check!")

print(f"Your score is {grade}:")
if grade >=55:
    print("You passed!")
else: 
    print("Try it again next time and focus on your studies!")
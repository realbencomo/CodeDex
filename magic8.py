import random


print("Magic 8 Ball")
print("Ask a Yes or No question and the Magic 8 Ball will provide an answer for you")

while True:
    question = input("Ask away: ...")
    num = random.randint(1, 9)

    if num == 1:
        print("Yes - definitely.")
    elif num == 2:
        print("It is decidedly so.")
    elif num == 3:
        print("Without a doubt.")
    elif num == 4:
        print("Reply hazy, try again.")
    elif num == 5:
        print("Ask again later.")
    elif num == 6:
        print("Better not tell you now.")
    elif num == 7:
        print("My sources say no")
    elif num == 8: 
        print("Outlook not so good.")
    elif print == 9:
        print("Very doubtful.")

    repeat = input("Want to play again? Y/N").upper()
    if repeat == "Y":
      continue
    else:
      break
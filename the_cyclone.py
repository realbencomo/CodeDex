while True:
    height = float(input("What's your height in cm? "))
    credits = float(input("How many credits do you have left? "))
    
    if height > 137 and credits > 10:
        print("Welcome aboard THE CYCLONE")
    elif height > 137 and credits < 10: 
        print("Not enough credits")
    elif height < 137 and credits > 10:
        print("You're not tall enough. Perhaps spend your credits in another game!")
    elif height < 137 and credits < 10:
        print("What are you doing here? Where are your parents?")
    
    repeat = input("Try again? Y/N: ").upper()
    if repeat == "Y":
        continue
    else:
        break

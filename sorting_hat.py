print("Welcome newly wizards to the renowned Sorting Hat\n")
print("Remember to answer truthfully and accurately\n")

while True:
    griffindor = 0
    slytherin = 0
    ravenclaw = 0
    hufflepuff = 0
    
    q1 = int(input("Q1) Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\n"))
    if q1 == 1:
        griffindor += 1
        hufflepuff += 1
    elif q1 == 2:
        slytherin += 1
        ravenclaw += 1
    else: 
        print("Wrong input!")

    q2 = int(input("Q2) When I'm dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n"))
    if q2 == 1:
        hufflepuff += 2
    elif q2 == 2:
        slytherin += 2
    elif q2 == 3:
        ravenclaw += 2
    elif q2 == 4:
        griffindor += 2
    else:
        print("Wrong input!")

    q3 = int(input("Q3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The harp\n3) The piano\n4) The cymbal\n"))
    if q3 == 1:
        slytherin += 4
    elif q3 == 2:
        hufflepuff += 4
    elif q3 == 3:
        griffindor += 4
    elif q3 == 4:
        ravenclaw += 4
    else:
        print("Wrong input!")

    print("Now for the time of truth!")
    if griffindor > max(slytherin, ravenclaw, hufflepuff):
        print("You're a 🦁 Gryffindor")
    elif slytherin > max(griffindor, ravenclaw, hufflepuff):
        print("You're a 🐍 Slytherin")
    elif hufflepuff > max(griffindor, ravenclaw, slytherin):
        print("You're a 🦡 Hufflepuff")
    elif ravenclaw > max(griffindor, hufflepuff, slytherin):
        print("You're a 🦅 Ravenclaw")
    else:
        print("It's a tie! You have traits from multiple houses.")
    
    repeat = input("Try again? Y/N: ").upper()
    if repeat == "Y":
        continue
    else:
        print("Goodbye young wizard!")
        break

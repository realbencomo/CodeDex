import random

symbols = ["🍒", "🍇", "🍉", "7️⃣"]

def results():
    
    spin = random.choices(symbols, k=3)
    print(spin)
    return spin

def play():
    counter = 200  
    while True:
        print("\nWelcome to the slot game!")
        print("This won't become addictive at all!\n")

        spin = results()  
        
       
        if spin == ["7️⃣", "7️⃣", "7️⃣"]:
            print("💲💲💲 Jackpot! 💰🤑 💲💲💲\n")
            print("➕💲2️⃣5️⃣0️⃣")
            counter += 250
        elif spin == ["🍒", "🍒", "🍒"]:
            print("🍒 Sweet cherries! 🍒 💲5️⃣0️⃣\n")
            counter += 50
        elif spin == ["🍇", "🍇", "🍇"]:
            print("🍇 The grapes of wrath! 🍇 ➕💲7️⃣5️⃣\n")
            counter += 75
        elif spin == ["🍉", "🍉", "🍉"]:
            print("🍉 Watermelon sweetness! 🍉 ➕💲1️⃣0️⃣0️⃣\n")
            counter += 100
        else:
            print("Better luck next time!\n")
            counter -= 25

       
        print(f'Your current balance is: 💲{counter} coins!\n')
        
        
        if counter <= 0:
            print("You're out of coins! Game over. 💀💀💀")
            break
        if counter >= 1000:
            print("We're going to have a chat with you, the house isn't supposed to lose...")
            print("😱✨✨✨✨🔫")
            break
        game = input("Play again? Y/N: ").upper()
        if game == "Y":
            continue
        else:
            print("Thanks for playing! Bye!\n")
            print(f'Your final coin count is: 💲{counter} coins!')
            break

play()

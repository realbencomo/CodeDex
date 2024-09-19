import random

options = [
  'Don’t pursue happiness – create it.',
  'All things are difficult before they are easy.',
  'The early bird gets the worm, but the second mouse gets the cheese.',
  'If you eat something and nobody sees you eat it, it has no calories.',
  'Someone in your life needs a letter from you.',
  'Don’t just think. Act!',
  'Your heart will skip a beat.',
  'The fortune you search for is in another cookie.',
  'Help! I’m being held prisoner in a Chinese bakery!'
]

def fortune():
    random_fortune = random.randint(0, len(options)-1)
    print(options[random_fortune])
    print()

while True:
    print ("🥠Fortune Cookie🥠\n\nYou open a Fortune Cookie!\n\nYour fortune is:\n")
    fortune()
    tryagain = input("Open another cookie? Y/N\n").upper()
    if tryagain == 'Y':
        continue
    else:
        break
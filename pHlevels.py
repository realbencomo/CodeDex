print("pH acidity and basicity test")
print()
acidity = float(input("What's the pH of the liquid? Remember that values range from 0 to 14..."))
if acidity >7:
  print("It's a BASIC liquid")
    
elif acidity <7:
  print("It's an ACID liquid")
else:
  print("It's a NEUTRAL liquid")
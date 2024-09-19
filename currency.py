print("You went to Colombia, Peru and Brazil. The leftover cash will be changed to USD")
print()
col = float(input("How much Colombian Pesos do you have left?"))
sol = float(input("How many Peruvian Soles do you have left?"))
rea = float(input("How many Brazilian Reais do you have left?"))

dllR = (col*0.00024)+(sol*0.27)+(rea*0.18)

print(f"You have USD$-{dllR}-$USD left! Be sure to exchange them!")
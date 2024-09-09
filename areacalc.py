while True:
    print("====================================")
    print("📐 Welcome to the area calculator 📏")
    print("====================================")
    shape = int(input("Choose your shape:\n1)Square\n2)Rectangle\n3)Triangle\n4)Circle\n5)Exit\n\n"))
    if shape == 1:
        print("A square it is!")
        sqside = float(input("Input the lenght of the side:\n"))
        sqarea = sqside**2
        print(f"The area is: {sqarea:.4f}")
        
                
    elif shape == 2:
        print("A rectangle it is\n")
        rctbase = float(input("What's the base of the rectangle?\n"))
        rctheight = float(input("What's the height of the rectangle?\n"))
        rctarea = rctbase * rctheight
        print(f"The area is: {rctarea:.4f}")
    
    elif shape == 3:
        print("A triangle it is\n")
        trglbase = float(input("What's the base of the triangle?\n"))
        trglheight = float(input("What's the height of the triangle?\n"))
        trglarea = (trglbase * trglheight)/2
        print(f"The area of the triangle is: {trglarea:.4f}")

    elif shape == 4:
        print ("A circle it is\n")
        crclrad = float(input("What's the radius of the circle? Remember that the radius is half the diameter!"))
        crclarea = (crclrad ** 2) * 3.14159
        print (f"The approximate area of the circle is: {crclarea:.4f}")
    
    elif shape == 5:
        print ("Thanks for using the area calculator, bye!")
        break


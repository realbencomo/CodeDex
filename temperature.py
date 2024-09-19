fahrenheit = float(input("What's the temperature at your location in Fahrenheit degrees? "))

def celDeg(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

celsius = celDeg(fahrenheit)

print(f"The temperature is: {celsius:.2f} degrees Celsius.")

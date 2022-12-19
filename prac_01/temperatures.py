"""
Temperature conversion
Pseudocode
display MENU
get choice
while choice != Q
    if choice = c
        get celsius
        fahrenheit = celsius * 9.0 / 5 + 32
        display fahrenheit
    else if choice =f
        get fahrenheit_temperature
        convert_celsius= 5/9*(fahrenheit_temperature - 32)
        display convert_celsius
else
    display Invalid Option
    get choice
display Thank you
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit_temperature = float(input("Fahrenheit: "))
        convert_celsius = 5/9*(fahrenheit_temperature - 32)
        print(f"Result: {convert_celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
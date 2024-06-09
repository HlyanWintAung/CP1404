# Questions
# When will a ValueError occur?
# A ValueError will occur if the input for the numerator or denominator is not a valid integer.

# When will a ZeroDivisionError occur?
# A ZeroDivisionError will occur if the denominator is zero. This has been handled by checking if the denominator is zero before performing the division.

# Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes, we can check if the denominator is zero before performing the division and handle it appropriately.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
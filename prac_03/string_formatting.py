name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# Using .format()
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))
print("My {} would cost ${:,.2f}!".format(name, cost))

# Aligning columns
numbers = [1, 19, 123, 456, 7890]
for number in numbers:
    print("Number is {:>5}".format(number))

# Example string formatting using f-strings
print(f"My guitar: {name}, first made in {year}")
print(f"My {name} was first made in {year} (that's right, {year}!)")
print(f"My {name} would cost ${cost:,.2f}!")

# Aligning columns with f-strings
for number in numbers:
    print(f"Number is {number:>6}")

# Task: Use f-string formatting to produce the output
print(f"{year} {name} for about ${cost:,.0f}!")

# Task: Using a for loop with the range function and f-string formatting
for i in range(11):
    print(f"2 ^ {i:2} is {2**i:4}")
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print(numbers)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")

average = sum(numbers) / len(numbers)
print(f"The average of the number is {average}")


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter user name: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
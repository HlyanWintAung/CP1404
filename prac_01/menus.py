
"""
get name
display menu
get choice
while choice != q
    if choice = h
        display name
        display menu
        get choice
    else if choice = g
        display name
        display menu
        get choice
else
    display Finished.
"""
menu = """(H)ello
(G)oodbye
(Q)uit"""
name = input("Enter name: ")
print(menu)
choice = input(">>> ").lower()
while choice != "q":
    if choice == "h":
        print(f"Hello {name}")
        print(menu)
        choice = input(">>> ").lower()
    elif choice == "g":
        print(f"Goodbye {name}")
        print(menu)
        choice = input(">>> ").lower()
else:
    print("Finished.")
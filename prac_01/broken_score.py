"""
get score
if score < 0
    display Invalid score
else:
    if score > 100:
        display Invalid score
    elif score > 50:
        display Passable
    elif score > 90:
        display Excellent
    else:
        display Bad

"""
score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    elif score > 50:
        print("Passable")
    elif score > 90:
        print("Excellent")
    else:
        print("Bad")
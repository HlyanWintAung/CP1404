def main():
    score = int(input("Enter your score: "))
    print(define_score(score))


def define_score(score):
    if score < 0:
        print("Invalid score")
    else:
        if score > 100:
            return "Invalid score"
        elif score > 90:
            return "Excellent"
        elif score > 50:
            return "Passable"
        else:
            return "Bad"


main()
def main():
    score = get_valid_score()
    print("(G)et a vaild score\n(P)rint result\n(S)how stars\n(Q)uit")
    choice = input("Select the option: ")
    if choice == "G":
        get_valid_score()
    elif choice == "P":
        score = int(input("Enter your score: "))
        print(define_score(score))
    elif choice == "S":
        stars(score)
    elif choice == "Q":
        print("Thank you")
    else:
        print("Invalid choice.Please select a vaild choice")




def stars(score):
    print("*" * score)



def define_score(score):
    if score < 0:
        print("Invalid score")
    else:
        if score > 100:
            return "Invalid score"
        elif score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"




def get_valid_score():
    score = int(input("Enter the score(0-100 inclusive): "))
    if 0 <= score <= 100:
        return score
    else:
        print("Score must be 0-100")


main()

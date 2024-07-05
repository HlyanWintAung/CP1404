"""
Assignment 1 for CP1404/CP5632, IT@JCU

By:Hlyan Wint Aung
"""


import csv

FILENAME = 'books.csv'
MENU = """
Menu:
D - Display books
A - Add a new book
C - Complete a book
Q - Quit
>>> """


def main():
    books = load_books()
    print("Books to Read 1.0 by Hlyan Wint Aung")
    print(f"{len(books)} books loaded.")

    while True:
        choice = input(MENU).strip().lower()
        if choice == 'd':
            print("")
            display_books(books)
        elif choice == 'a':
            add_book(books)
        elif choice == 'c':
            complete_book(books)
        elif choice == 'q':
            save_books(books)
            print("Books saved to books.csv\n\"So many books, so little time. Frank Zappa\"")
            break
        else:
            print("Invalid menu choice")



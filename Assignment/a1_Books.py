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




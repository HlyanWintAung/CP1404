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


def load_books():
    books = []
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                row[2] = int(row[2])
                books.append(row)
    except FileNotFoundError:
        print(f"File {FILENAME} not found. Starting with an empty list.")
    return books


def display_books(books):
    if not books:
        print("No books to display.")
    else:
        books.sort(key=lambda book: (book[1], book[0]))
        total_pages = 0
        unread_books = 0

        for i in range(len(books)):
            book = books[i]
            if book[3] == 'u':
                status = '*'
                total_pages += book[2]
                unread_books += 1
            else:
                status = ' '

            print(f"{status}{i + 1}. {book[0]:<30} by {book[1]:<20} {book[2]} pages")

        print(f"You still need to read {total_pages} pages in {unread_books} books.")


def add_book(books):
    title = get_non_empty_string("Title: ")
    author = get_non_empty_string("Author: ")
    pages = get_positive_int("Number of Pages: ")
    books.append([title, author, pages, 'u'])
    print(f"{title} by {author} ({pages} pages) added.")



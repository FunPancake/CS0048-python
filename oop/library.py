# Library Management System

# - A library has books with attributes like title, author, and availability. 
# - Users can add books, borrow books, return books, and view all books in the library. 
# - The program should provide a menu for users to select actions (e.g., Add Book, Borrow Book, Return Book, View Books). 
# - Use classes for Book and Library.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"Title: {self.title}, Author: {self.author}, Status: {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print("Book added successfully!")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print("Book borrowed successfully!")
                return
        print("Book is either not available or doesn't exist.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print("Book returned successfully!")
                return
        print("Book not found or already available.")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nLibrary Books:")
            for book in self.books:
                print(book)


def main():
    library = Library()
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == '2':
            title = input("Enter the title of the book to borrow: ")
            library.borrow_book(title)
        elif choice == '3':
            title = input("Enter the title of the book to return: ")
            library.return_book(title)
        elif choice == '4':
            library.view_books()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
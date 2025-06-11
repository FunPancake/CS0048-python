# Library Management System

# - A library has books with attributes like title, author, and availability. 
# - Users can add books, borrow books, return books, and view all books in the library. 
# - The program should provide a menu for users to select actions (e.g., Add Book, Borrow Book, Return Book, View Books). 
# - Use classes for Book and Library.

class Book:
    def __init__(self, title, author,):
        self.title = title
        self.author = author
        self.available = True
    
    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"Title: {self.title}, Author: {self.author}, Status: {status}"
    
class Library:
    def __init__(self):
        self.books = []
        
    def addbook(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print("Book is Added in the Library")
        
    def borrowbook(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print("Book is successfully Borrowed ")
                return
        print("Book is not in Available")
        
    def returnbook(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print("Book is successfully Returned")
                return
        print("Book is Already In the Library")
        
    def viewbook(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nLibrary Books:")
            for book in self.books:
                print(book)

def main():
    library = Library()
    while True:
        print ("\nLibrary Management System ")
        print ("1. Add Book ")
        print ("2. Borrow Book ")
        print ("3. Return Book ")
        print ("4. View all Books ")
        print ("5. Exit")

        choice = input ("Enter your choice 1-4: ")
        
        if choice == '1':
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            library.addbook(title, author)
        
        elif choice == '2':
            title = input("Enter the title of the book to borrow: ")
            library.borrowbook(title)
            
        elif choice == '3':
            title = input("Enter the title of the book to return: ")
            library.returnbook(title)
            
        elif choice == '4':
            library.viewbook()
            
        elif choice == '5':
            print ("exit program")
            break 
    
        else:
            print ("Invalid choice")

if __name__ == "__main__":
    main()

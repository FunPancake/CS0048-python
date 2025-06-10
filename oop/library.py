# Library Management System

# - A library has books with attributes like title, author, and availability. 
# - Users can add books, borrow books, return books, and view all books in the library. 
# - The program should provide a menu for users to select actions (e.g., Add Book, Borrow Book, Return Book, View Books). 
# - Use classes for Book and Library.

class Library:
    def __init__(title, author):
        self.title = title
        self.author = author

class Book:
    def __init__(title, author):
        self.title = title
        self.author = author
class Book:
    # Constructor for the Book class
    def __init__(self, title, author):
        self.title = title  # Title of the book
        self.author = author  # Author of the book

    # String representation of the Book object
    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    # Constructor for the Library class
    def __init__(self):
        self.books = []  # Initialize an empty list to hold books

    # Method to add a book to the library
    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book}")

    # Method to remove a book from the library
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Removed book: {title}")
                break
        else:
            print("Book not found!")

    # Method to display all books in the library
    def list_books(self):
        if self.books:
            print("Library contains the following books:")
            for book in self.books:
                print(book)
        else:
            print("No books in the library!")

def main():
    library = Library()  # Create a library instance
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(Book(title, author))
        elif choice == '2':
            title = input("Enter book title to remove: ")
            library.remove_book(title)
        elif choice == '3':
            library.list_books()
        elif choice == '4':
            print("Exiting the library system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

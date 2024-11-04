class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books = []
    def add_books(self, book):
        self.books.append(book)
        print(f"{book} Has been added")

    def remove_books(self,title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"{book} has been removed")
                break
            else:
                print("Book not found")
    def list_books(self):
        print("library contain these books: ")
        for book in self.books:
            print(book)

def main():
    library = Library()
    while True:
        print("\n Library Management system")
        print("1. Add Books")
        print("2. Remove Books")
        print("3. Book List")
        print("4. Exit")
        choice = input("Enter Your Choice: ")

        if choice == '1':
            title = input("Enter Book Title: ")
            author = input("Enter book author: ")
            library.add_books(Book(title,author))
        elif choice == '2':
            title = input("Enter Book Title: ")
            library.remove_books(title)
        elif choice == '3':
            library.list_books()

        elif choice == '4':
            print("Exited Successfully")
            break


if __name__ == '__main__':
    main()

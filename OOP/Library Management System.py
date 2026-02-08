class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You borrowed '{self.title}'")
        else:
            print("Book already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You returned '{self.title}'")
        else:
            print("Book was not borrowed.")


class Library:
    def __init__(self):
        self.books = []   # empty list to store Book objects

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        new_book = Book(title, author)   # create object
        self.books.append(new_book)      # append object to list

        print("Book added successfully!\n")

    def show_books(self):
        if not self.books:
            print("No books in library.")
        else:
            print("\nLibrary Books:")
            for book in self.books:
                status = "Available" if not book.is_borrowed else "Borrowed"
                print(f"{book.title} by {book.author} - {status}")


library = Library()

while True:
    print("\n1. Add Book")
    print("2. Show Books")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.show_books()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")

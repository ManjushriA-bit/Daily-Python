class Library:
    def __init__(self):
        self.books = ["python", "java", "c++"]

    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\nBooks available:")
        for book in self.books:
            print("-", book.title())

    def add_book(self):
        new_book = input("Enter the new book name: ").strip().lower()

        if new_book in self.books:
            print(f"{new_book.title()} book already exists.")
        else:
            self.books.append(new_book)
            print(f"{new_book.title()} book added successfully!")

    def borrow_book(self):
        book_name = input("Enter book name to borrow: ").strip().lower()

        if book_name in self.books:
            self.books.remove(book_name)
            print(f"{book_name.title()} book borrowed successfully!")
        else:
            print(f"{book_name.title()} book not available.")


def menu():
    print("\n1. Display books")
    print("2. Add new book")
    print("3. Borrow a book")
    print("4. Exit")


library = Library()

while True:
    menu()
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            library.display_books()
        elif choice == 2:
            library.add_book()
        elif choice == 3:
            library.borrow_book()
        elif choice == 4:
            print("Thank you for using the library system!")
            break
        else:
            print("Invalid choice. Please select 1–4.")

    except ValueError:
        print("Please enter a valid number.")

class Book:
    def __init__(self, title, author, availability=True):
        self.title = title
        self.author = author
        self.availability = availability

    def checkout(self):
        if self.availability:
            self.availability = False
            print(f"You have successfully checked out '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' is currently unavailable.")

    def return_book(self):
        if not self.availability:
            self.availability = True
            print(f"Thank you for returning '{self.title}'.")
        else:
            print(f"'{self.title}' was not checked out.")

    def __str__(self):
        return f"'{self.title}' by {self.author} - {'Available' if self.availability else 'Checked out'}"


class Catalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to the catalog.")

    def display_books(self):
        if not self.books:
            print("No books in the catalog yet.")
        else:
            for book in self.books:
                print(book)

# Sample Interaction:
if __name__ == "__main__":
    # Create a catalog
    catalog = Catalog()

    # Add new books
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", False)  # already checked out

    catalog.add_book(book1)
    catalog.add_book(book2)
    catalog.add_book(book3)

    # Display all books in the catalog
    print("\nBooks in the Catalog:")
    catalog.display_books()

    # Checkout some books
    print("\nChecking out '1984':")
    book1.checkout()  # Should succeed

    print("\nChecking out 'The Great Gatsby':")
    book3.checkout()  # Should fail as it is already checked out

    # Return a book
    print("\nReturning '1984':")
    book1.return_book()  # Should succeed

    # Display all books again
    print("\nBooks in the Catalog after some actions:")
    catalog.display_books()

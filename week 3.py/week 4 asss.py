class Book:
    def __init__(self, title, author, isbn, year):
        """Constructor to initialize Book attributes."""
        self.title = title
        self.author = author
        self._isbn = isbn  # Encapsulated attribut
        self.is_available = True

    def read(self):
        """Base method for reading the book (to be overridden)."""
        return f"Reading '{self.title}' by {self.author}."

    def get_details(self):
        """Method to return book details, including protected ISBN."""
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self._isbn}, Year: {self.year}"

    def check_out(self):
        """Method to mark book as unavailable."""
        if self.is_available:
            self.is_available = False
            return f"'{self.title}' has been checked out."
        return f"'{self.title}' is already checked out."

    def return_book(self):
        """Method to mark book as available."""
        if not self.is_available:
            self.is_available = True
            return f"'{self.title}' has been returned."
        return f"'{self.title}' is already available."


class EBook(Book):
    def __init__(self, title, author, isbn, year, file_size):
        """Constructor for EBook, extending Book."""
        super().__init__(title, author, isbn, year)
        self.file_size = file_size  # Size in MB

    def read(self):
        """Polymorphic method overriding read for EBook."""
        return f"Reading '{self.title}' digitally on your device ({self.file_size} MB)."


class PhysicalBook(Book):
    def __init__(self, title, author, isbn, year, page_count):
        """Constructor for PhysicalBook, extending Book."""
        super().__init__(title, author, isbn, year)
        self.page_count = page_count

    def read(self):
        """Polymorphic method overriding read for PhysicalBook."""
        return f"Reading '{self.title}' in print, flipping through {self.page_count} pages."


# Example usage to demonstrate functionality
def main():
    # Create instances of different books
    ebook = EBook("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 1925, 2.5)
    physical_book = PhysicalBook("1984", "George Orwell", "978-0451524935", 1949, 328)

    # Demonstrating polymorphism with read method
    books = [ebook, physical_book]
    print("Reading Books:")
    for book in books:
        print(f"- {book.read()}")

    # Demonstrating encapsulation and other methods
    print("\nBook Details:")
    print(ebook.get_details())
    print(physical_book.get_details())

    # Demonstrate checkout and return functionality
    print("\nLibrary Actions:")
    print(ebook.check_out())
    print(ebook.check_out())  # Already checked out
    print(ebook.return_book())
    print(physical_book.check_out())


if __name__ == "__main__":
    main()
    
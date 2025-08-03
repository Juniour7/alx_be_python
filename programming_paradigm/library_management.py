class Book:
    """
    Represents a single book in the library.
    Each book has a title, an author, and a status indicating whether it is checked out.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """
        Checks if the book is available.
        Returns:
            bool: True if the book is available, False otherwise.
        """
        return not self._is_checked_out


class Library:
    """
    Represents a library, which manages a collection of Book objects.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty collection of books.
        """
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.
        Args:
            book (Book): The Book instance to add.
        """
        self._books.append(book)

    def find_book(self, title):
        """
        Finds a book in the library by its title.
        Args:
            title (str): The title of the book to find.
        Returns:
            Book or None: The Book object if found, otherwise None.
        """
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title):
        """
        Checks out a book from the library by its title.
        Finds the book and marks it as checked out.
        Args:
            title (str): The title of the book to check out.
        """
        book = self.find_book(title)
        if book:
            book.check_out()
        else:
            print(f"Sorry, the book '{title}' was not found in the library.")

    def return_book(self, title):
        """
        Returns a book to the library by its title.
        Finds the book and marks it as returned.
        Args:
            title (str): The title of the book to return.
        """
        book = self.find_book(title)
        if book:
            book.return_book()
        else:
            print(f"Sorry, the book '{title}' was not found in the library.")

    def list_available_books(self):
        """
        Prints a list of all available books in the library.
        """
        available_books_found = False
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
                available_books_found = True
        if not available_books_found:
            # This part is not in the required output but is good practice
            print("No books are currently available.")
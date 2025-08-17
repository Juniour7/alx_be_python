class Book:
    """
    A base class to represent a book with a title and an author.
    """
    def __init__(self, title: str, author: str):
        """Initializes the Book instance."""
        self.title = title
        self.author = author

    def display(self):
        """Prints the basic details of the book."""
        print(f"Book: {self.title} by {self.author}")

class EBook(Book):
    """
    A derived class for electronic books, inheriting from Book.
    """
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes the EBook instance, calling the base class constructor
        and setting the file size.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def display(self):
        """Prints the details of the EBook, including file size."""
        print(f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB")

class PrintBook(Book):
    """
    A derived class for printed books, inheriting from Book.
    """
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes the PrintBook instance, calling the base class constructor
        and setting the page count.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def display(self):
        """Prints the details of the PrintBook, including page count."""
        print(f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}")

class Library:
    """
    A class to represent a library, which is composed of a collection of books.
    """
    def __init__(self):
        """Initializes the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """
        Adds a Book, EBook, or PrintBook instance to the library's collection.
        
        Args:
            book: An instance of Book or its subclasses.
        """
        self.books.append(book)

    def list_books(self):
        """
        Iterates through the collection of books and prints their details.
        """
        for book in self.books:
            book.display() # Polymorphism in action!
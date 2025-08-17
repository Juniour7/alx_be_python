class Book:
    """
    A class to represent a book with title, author, and publication year.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Initializes a Book instance with a title, author, and year.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Creating '{self.title}'")

    def __del__(self):
        """
        Prints a message when the Book instance is being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self) -> str:
        """
        Returns a user-friendly string representation of the Book instance.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """
        Returns an official string representation that can recreate the Book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
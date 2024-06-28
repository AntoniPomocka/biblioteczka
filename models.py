import json

class Book:
    """Represents a book in the library."""
    def __init__(self, title, author, genre, rating):
        self.title = title
        self.author = author
        self.genre = genre
        self.rating = rating

    def to_dict(self):
        """Converts the book object to a dictionary."""
        return {
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "rating": self.rating,
        }

class Books:
    """Handles book data persistence."""
    def __init__(self):
        try:
            with open("books.json", "r") as f:
                self.books = [Book(**book_data) for book_data in json.load(f)]
        except FileNotFoundError:
            self.books = []

    def all(self):
        """Returns a list of all books."""
        return self.books

    def get(self, id):
        """Returns a book by its ID."""
        return self.books[id]

    def create(self, book):
        """Adds a new book to the list."""
        self.books.append(book)

    def update(self, id, book):
        """Updates an existing book by its ID."""
        self.books[id] = book
        self.save_all()

    def save_all(self):
        """Saves all books to the JSON file."""
        with open("books.json", "w") as f:
            json.dump([book.to_dict() for book in self.books], f)

books = Books()
from flask import Flask, jsonify, request
from models import Book, books

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_books():
        """Returns a list of all books."""
        all_books = books.all()
        book_list = [book.to_dict() for book in all_books]
        return jsonify(book_list)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
        """Returns details of a specific book by ID."""
        book = books.get(book_id - 1)
        if book:
            return jsonify(book.to_dict())
        else:
            return jsonify({'error': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def add_book():
        """Adds a new book to the library."""
        data = request.get_json()
        if 'title' not in data or 'author' not in data or 'genre' not in data or 'rating' not in data:
            return jsonify({'error': 'Missing required fields'}), 400

        book = Book(
            title=data['title'],
            author=data['author'],
            genre=data['genre'],
            rating=data['rating'],
        )
        books.create(book)
        books.save_all()
        return jsonify(book.to_dict()), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
        """Updates an existing book by ID."""
        book = books.get(book_id - 1)
        if book:
            data = request.get_json()
            if 'title' in data:
                book.title = data['title']
            if 'author' in data:
                book.author = data['author']
            if 'genre' in data:
                book.genre = data['genre']
            if 'rating' in data:
                book.rating = data['rating']
            books.update(book_id - 1, book)
            return jsonify(book.to_dict())
        else:
            return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
        """Deletes a book by ID."""
        book = books.get(book_id - 1)
        if book:
            books.books.pop(book_id - 1)
            books.save_all()
            return jsonify({'message': 'Book deleted'}), 204
        else:
            return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
        app.run(debug=True)
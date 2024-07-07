from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddBookForm, UpdateBookForm
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Book, Author, BorrowRecord

@app.route('/')
def index():
    books = Book.query.order_by(Book.title).all()  
    recent_books = Book.query.order_by(Book.id.desc()).limit(5).all()
    return render_template('index.html', books=books, recent_books=recent_books)

@app.route('/books', methods=['GET', 'POST'])
def add_book():
    form = AddBookForm()
    try:
        if form.validate_on_submit():
            author_names = [name.strip() for name in form.authors.data.split(',')]
            authors = []
            for name in author_names:
                author = Author.query.filter_by(name=name).first()
                if not author:
                    author = Author(name=name)
                authors.append(author)
            book = Book(title=form.title.data,
                        authors=authors,
                        genre=form.genre.data,
                        rating=form.rating.data)
            db.session.add(book)
            db.session.commit()
            flash('Książka dodana pomyślnie!')
            return redirect(url_for('index'))
    except Exception as e:
        db.session.rollback()
        app.logger.error(f'Wystąpił błąd: {str(e)}')
        flash(f'Wystąpił błąd: {str(e)}', 'error')
    return render_template('add_book.html', form=form)

@app.route('/books/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    form = UpdateBookForm()
    if form.validate_on_submit():
        book.title = form.title.data
        author_names = [name.strip() for name in form.authors.data.split(',')]
        authors = []
        for name in author_names:
            author = Author.query.filter_by(name=name).first()
            if not author:
                author = Author(name=name)
            authors.append(author)
        book.authors = authors
        book.genre = form.genre.data
        book.rating = form.rating.data
        db.session.commit()
        flash('Książka zaktualizowana pomyślnie!')
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.title.data = book.title
        form.authors.data = ', '.join(author.name for author in book.authors)
        form.genre.data = book.genre
        form.rating.data = book.rating
    return render_template('update_book.html', form=form, book=book)

@app.route('/books/<int:book_id>/details')
def book_details(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book_details.html', book=book)

@app.route('/books/<int:book_id>/borrow', methods=['POST'])
def borrow_book(book_id):
    book = Book.query.get_or_404(book_id)
    borrow_record = BorrowRecord(book_id=book.id, borrowed=True)
    db.session.add(borrow_record)
    db.session.commit()
    flash('Książka wypożyczona pomyślnie!')
    return redirect(url_for('index'))

@app.route('/books/<int:borrow_id>/return', methods=['POST'])
def return_book(borrow_id):
    borrow_record = BorrowRecord.query.get_or_404(borrow_id)
    borrow_record.returned = True
    db.session.commit()
    flash('Książka zwrócona pomyślnie!')
    return redirect(url_for('index'))

@app.route('/books/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    flash('Książka została usunięta!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
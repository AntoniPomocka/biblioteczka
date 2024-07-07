from app import db

book_author = db.Table('book_author',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'))
)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    authors = db.relationship('Author', secondary=book_author, backref='books')
    genre = db.Column(db.String(64))
    rating = db.Column(db.Integer)
    borrow_records = db.relationship('BorrowRecord', backref='book')

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)

class BorrowRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    borrowed = db.Column(db.Boolean, default=False)
    returned = db.Column(db.Boolean, default=False)
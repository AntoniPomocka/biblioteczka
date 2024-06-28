from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
from flask_wtf import FlaskForm

class AddBookForm(FlaskForm):
    """Form for adding a new book."""
    title = StringField("Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    genre = StringField("Genre", validators=[DataRequired()])
    rating = IntegerField("Rating (1-5)", validators=[DataRequired()])
    submit = SubmitField("Add Book")

class UpdateBookForm(FlaskForm):
    """Form for updating an existing book."""
    title = StringField("Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    genre = StringField("Genre", validators=[DataRequired()])
    rating = IntegerField("Rating (1-5)", validators=[DataRequired()])
    submit = SubmitField("Update Book")
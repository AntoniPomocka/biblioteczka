from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, NumberRange

class AddBookForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    authors = TextAreaField('Autorzy', validators=[DataRequired()])
    genre = SelectField('Gatunek', choices=[
        ('Fantastyka', 'Fantastyka'),
        ('Obyczajowa', 'Obyczajowa'),
        ('Kryminał', 'Kryminał'),
        ('Horror', 'Horror'),
        ('Romans', 'Romans'),
        ('Sci-fi', 'Sci-fi'),
        ('Biografia', 'Biografia'),
        ('Historia', 'Historia')
    ], validators=[DataRequired()])
    rating = IntegerField('Ocena', validators=[DataRequired(), NumberRange(min=1, max=10)])
    submit = SubmitField('Dodaj książkę')

class UpdateBookForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    authors = TextAreaField('Autorzy', validators=[DataRequired()])
    genre = SelectField('Gatunek', choices=[
        ('Fantastyka', 'Fantastyka'),
        ('Obyczajowa', 'Obyczajowa'),
        ('Kryminał', 'Kryminał'),
        ('Horror', 'Horror'),
        ('Romans', 'Romans'),
        ('Sci-fi', 'Sci-fi'),
        ('Biografia', 'Biografia'),
        ('Historia', 'Historia')
    ], validators=[DataRequired()])
    rating = IntegerField('Ocena', validators=[DataRequired(), NumberRange(min=1, max=10)])
    submit = SubmitField('Zaktualizuj książkę')
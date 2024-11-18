# Lee Fawkes
# SDEV 220 - Andrew Emily
# Module 4 Lab - Python APIs


from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(40))

    def __repr__(self):
        return f"{self.name}, {self.author}, {self.publisher}"

@app.route('/')
def index():
    return "Hello!"

@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'name': book.name, 'author': book.author, 'publisher': book.publisher }

        output.append(book_data)
    return {"books": output}
from flask import Flask, render_template
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Books(db.Model):
    bookID = db.Column(db.String(250), primary_key=True)
    title = db.Column(db.String(250))
    authors = db.Column(db.String(250))
    average_rating = db.Column(db.String(250))
    isbn = db.Column(db.String(250))
    isbn13 = db.Column(db.String(250))
    language_code = db.Column(db.String(250))
    num_pages = db.Column(db.String(250))
    ratings_count = db.Column(db.String(250))
    text_reviews_count = db.Column(db.String(250))
    publication_date = db.Column(db.String(250))
    publisher = db.Column(db.String(250))
    stock = db.Column(db.Integer)
    borrowed_by = db.Column(db.String(200))  # TODO: needs to change unit


class Members(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    outstanding_debt = db.Column(db.String(100))
    borrowed_books = db.Column(db.String(200))  # TODO: needs to change unit


url = 'https://frappe.io/api/method/frappe-library'
response = requests.get(url)
obj = response.json().get('message')


def remove_dict_key_whitespaces(dictionary):
    return {k.translate({32: None}): v for k, v in dictionary.items()}


def add_to_database(list_of_dicts):
    if Books.query.count() > 0:
        return
    for d in list_of_dicts:
        book_item = remove_dict_key_whitespaces(d)
        book_entry = Books(**book_item)
        db.session.add(book_entry)
        db.session.commit()


add_to_database(obj)


@app.route('/')
def helloworld():
    return render_template("home.html")


@app.route('/books')
def book():
    list_of_books = Books.query.all()
    return render_template("books.html", books=list_of_books)


@app.route('/members')
def members():
    return render_template("members.html")


@app.route('/transactions')
def transactions():
    return render_template("transactions.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

from flask import Flask, render_template
import requests
from flask_sqlalchemy import SQLAlchemy

# books, members, transactions

app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class Books(db.Model):
    _id = db.Column("bookID", db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    authors = db.Column(db.String(250))
    isbn = db.Column(db.Integer)
    publisher = db.Column(db.String(250))
    stock = db.Column(db.Integer)
    borrowed_by = db.Column(db.String(200))  # TODO: needs to change unit
    # TODO: add pages


class Members(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    outstanding_debt = db.Column(db.String(100))
    borrowed_books = db.Column(db.String(200))  # TODO: needs to change unit


url = 'https://frappe.io/api/method/frappe-library'


def join_string(text):
    return text


response = requests.get(url)
obj = response.json().get('message')
mapped_obj = list(map(join_string, obj))
books = Books(**{k: obj[k] for k in ('bookID', 'title', 'authors', 'isbn', 'publisher') if k in obj})


@app.route('/')
def helloworld():
    return 'Hello, world!'


@app.route('/books')
def book():
    return render_template("books.html", data=books)


@app.route('/members')
def members():
    return "Members!"


@app.route('/transactions')
def transactions():
    return "Transactions!"


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

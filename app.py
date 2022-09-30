from flask import Flask, render_template, request, redirect, url_for
import uuid
import requests
from flask_sqlalchemy import SQLAlchemy

# This assumes that one member can borrow one book at a time
# But a book can be borrowed by many members as long as
# there is sufficient stock of the book

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Books(db.Model):
    bookID = db.Column(db.String(250), primary_key=True, nullable=False)
    title = db.Column(db.String(250), nullable=False)
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
    no_of_copies_total = db.Column(db.Integer)
    no_of_copies_current = db.Column(db.Integer)
    borrowed_by = db.relationship('Members', backref='owner')


class Members(db.Model):
    memberID = db.Column("id", db.String(255), primary_key=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    outstanding_debt = db.Column(db.Integer)
    borrowed_from_date = db.Column(db.DateTime)
    borrowed_to_date = db.Column(db.DateTime)
    actual_return_date = db.Column(db.DateTime)
    book_id = db.Column(db.String(250), db.ForeignKey('books.bookID'))


class Transactions(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(20))
    title = db.Column(db.String(250))
    authors = db.Column(db.String(250))
    date_of_issue = db.Column(db.DateTime)
    due_date = db.Column(db.DateTime)
    date_of_return = db.Column(db.DateTime)


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
        book_entry = Books(**book_item, no_of_copies_total=1)
        db.session.add(book_entry)
        db.session.commit()


# add_to_database(obj)


@app.route('/')
def helloworld():
    return render_template("home.html")


@app.route('/books', methods=["GET"])
def books():
    list_of_books = Books.query.all()
    return render_template("books.html", books=list_of_books)


@app.route('/add-book', methods=["POST"])
def add_to_books():
    book_id = request.form.get('book_id')
    title = request.form.get('title')
    authors = request.form.get('authors')
    isbn = request.form.get('isbn')
    publisher = request.form.get('publisher')
    quantity = request.form.get('quantity')

    given_id = Books.query.filter_by(bookID=book_id).count()
    given_isbn = Books.query.filter_by(isbn=isbn).count()

    if given_id != 0 or given_isbn != 0:
        return "This book is already in stock"

    new_book = Books(bookID=book_id, title=title, authors=authors, isbn=isbn, publisher=publisher,
                     no_of_copies_total=quantity)
    db.session.add(new_book)
    db.session.commit()
    return redirect(url_for("books"))


@app.route('/delete-book/<string:book_id>')
def delete_book(book_id):
    book = Books.query.filter_by(bookID=book_id).first()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("books"))


@app.route('/members', methods=["GET"])
def members():
    list_of_members = Members.query.all()
    return render_template("members.html", members=list_of_members)


@app.route("/add-member", methods=["POST"])
def add_to_members():
    member_uuid = uuid.uuid4()
    member_id = str(member_uuid)
    username = request.form.get("username")
    rows = Members.query.filter_by(username=username).count()

    if rows != 0:
        return "Username is already taken"

    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    new_member = Members(memberID=member_id, username=username, first_name=first_name, last_name=last_name)
    db.session.add(new_member)
    db.session.commit()
    return redirect(url_for("members"))


@app.route('/delete-member/<string:member_id>')
def delete_member(member_id):
    member = Members.query.filter_by(memberID=member_id).first()
    db.session.delete(member)
    db.session.commit()
    return redirect(url_for("members"))


@app.route('/transactions', methods=["GET"])
def transactions():
    return render_template("transactions.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

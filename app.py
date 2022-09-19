from flask import Flask, render_template
import requests
import sqlalchemy

# books, members, transactions

app = Flask(__name__)

db = sqlalchemy(app)

url = 'https://frappe.io/api/method/frappe-library'

response = requests.get(url)
formatted_response = response.json()


class Books(db.Model):
    _id = db.Column("bookID", db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    authors = db.Column(db.String(250))
    isbn = db.Column(db.Integer)
    publisher = db.Column(db.String(250))
    borrowed_by = db.Column(db.String(200))  # TODO: needs to change unit
    # TODO: add pages


class Members(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    outstanding_debt = db.Column(db.String(100))
    borrowed_books = db.Column(db.String(200))  # TODO: needs to change unit


@app.route('/')
def helloworld():
    return 'Hello, world!'


@app.route('/books')
def book():
    return render_template("books.html", data=formatted_response)


@app.route('/members')
def members():
    return "Members!"


@app.route('/transactions')
def transactions():
    return "Transactions!"


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

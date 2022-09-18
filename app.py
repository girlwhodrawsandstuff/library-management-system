from flask import Flask, render_template

# books, members, transactions

app = Flask(__name__)

@app.route('/')
def helloworld():
    return 'Hello, world!'

@app.route('/books')
def book():
    return render_template("books.html")

@app.route('/members')
def members():
    return "Members!"

@app.route('/transactions')
def transactions():
    return "Transactions!"

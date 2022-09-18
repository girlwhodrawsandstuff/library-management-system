from flask import Flask

# books, members, transactions

app = Flask(__name__)

@app.route('/')
def helloworld():
    return 'Hello, world!'

@app.route('/members')
def members():
    return 'Members!'


@app.route('/books')
def books():
    return 'Books!'

@app.route('/transactions')
def books():
    return 'Transactions!'

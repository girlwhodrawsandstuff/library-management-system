from flask import Flask, render_template
import requests

# books, members, transactions

app = Flask(__name__)

url = 'https://frappe.io/api/method/frappe-library'

response = requests.get(url)
formatted_response = response.json()

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

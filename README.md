# Library Management System

*This is a library management system built using Python [Flask], JavaScript, HTML and CSS.*

Right now, this app assumes that it's only used by the librarian.

The librarian can maintain:
-   **Books**  with its stock
-   **Members**
-   **Transactions**

Here are some basic features
- Basic [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) operations can be done on books and members.
- Issue a book to a member
-  Issue a book return from a member
-   Search for a book by name and author
-   Charge a rent fee on book returns
-   Make sure a member’s outstanding debt is not more than Rs.500

This application uses the [Frappe API](https://frappe.io/api/method/frappe-library) to populate the database with it's default set of books. However, if a librarian wants to add other books, they can do so.

## How do I use this app?
You can simply access it [here](https://flask-library-system.herokuapp.com/).

## How do I run this project myself?

 1. Clone this repository
 2. Activate your virtualenv
 3. Run: `pip install -r requirements.txt` in your shell
 4. Run: `flask run`

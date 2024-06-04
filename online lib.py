import sqlite3

# Create a SQLite database or connect to an existing one
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create a table to store books
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        year INTEGER
    )
''')

# Function to add a book to the database
def add_book(title, author, year):
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    conn.commit()

# Function to view all books in the database
def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    for book in books:
        print(book)

# Function to search for a book by title
def search_book(title):
    cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
    book = cursor.fetchone()
    if book:
        print(book)
    else:
        print("Book not found.")

# Function to update a book's details
def update_book(id, title, author, year):
    cursor.execute("UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?", (title, author, year, id))
    conn.commit()

# Function to delete a book by ID
def delete_book(id):
    cursor.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a book")
    print("2. View all books")
    print("3. Search for a book")
    print("4. Update a book")
    print("5. Delete a book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = int(input("Enter publication year: "))
        add_book(title, author, year)
    elif choice == "2":
        view_books()
    elif choice == "3":
        title = input("Enter book title to search: ")
        search_book(title)
    elif choice == "4":
        id = int(input("Enter book ID to update: "))
        title = input("Enter new title: ")
        author = input("Enter new author: ")
        year = int(input("Enter new publication year: "))
        update_book(id, title, author, year)
    elif choice == "5":
        id = int(input("Enter book ID to delete: "))
        delete_book(id)
    elif choice == "6":
        conn.close()
        break
    else:
        print("Invalid choice. Please try again.")
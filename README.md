
# Library Management System

A Python-based Library Management System designed to help manage books in a library efficiently. This system allows librarians to add, issue, return, and manage books, as well as track overdue fines.

## Features
- **Add Books**: Librarians can add new books to the system by providing the book title, ID, and author.
- **Issue Books**: Books can be issued to students, and the issue date is tracked.
- **Return Books**: Books can be returned, and fines for overdue books are calculated.
- **Delete Books**: Damaged or outdated books can be deleted from the system.
- **Search Books**: Search for books by title or ID.
- **Display Books**: Display all books in the library or only available books.
- **Fine Calculation**: Automatically calculate fines for books returned after the due date.
- **Security**: The system is protected with a login system for authorized users.

## Requirements

### Software
- **Python**: Version 2.0 or above
- **MySQL**: Database for storing book records
- **Operating System**: Windows 7/8/10 or Unix Platform

### Hardware
- **RAM**: 2 GB minimum
- **Storage**: 1 GB HDD space
- **Processor**: Intel Pentium or greater
- **Screen Resolution**: 1366 x 768 (Optimal)
- **Graphics Card**: Minimum 64 MB

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/Library-Management-System.git
```

### Step 2: Install Dependencies
Make sure you have **MySQL** installed and set up on your system.

Install required Python packages:
```bash
pip install mysql-connector-python pandas
```

### Step 3: Database Setup
1. Open **MySQL** and create a new database called `librarymanagment_system`.
2. Run the following SQL queries (or run the back-end script provided) to create the required tables:
   ```sql
   CREATE TABLE books(BOOK_NAME VARCHAR(50), BOOK_ID VARCHAR(7), AUTHOR VARCHAR(50));
   CREATE TABLE available_books(BOOK_NAME VARCHAR(50), BOOK_ID VARCHAR(7), AUTHOR VARCHAR(50));
   CREATE TABLE issue(NAME VARCHAR(50), ADMIN_NO INT, BOOK_ID INT, ISSUE DATE);
   CREATE TABLE submit(NAME VARCHAR(50), ADMIN_NO INT, BOOK_ID INT, SUBMIT_DATE DATE);
   CREATE TABLE students(NAME VARCHAR(50), ADMIN_NO INT PRIMARY KEY NOT NULL, FINE_AMOUNT INT DEFAULT 0);
   CREATE TABLE books_to_be_submitted(NAME VARCHAR(50), ADMIN_NO INT, BOOK_ID INT, SUBMIT_DATE DATE);
   ```

### Step 4: Running the Application
Run the Python script:
```bash
python library_management_system.py
```

Follow the prompts to perform actions like adding, issuing, and returning books.

## Usage

### Main Menu
Once the program starts, you will be presented with a menu to perform the following tasks:
1. **Sign Up**: Register a new student.
2. **Add Book**: Add new books to the library.
3. **Issue Book**: Issue a book to a student.
4. **Submit Book**: Return a book and clear fines if applicable.
5. **Delete Books**: Remove a book from the library's collection.
6. **Display Books**: View all books or only available books.
7. **Search Books**: Search for books by ID or title.
8. **Fine Payment**: Pay fines for overdue books.
9. **Exit**: Exit the system.

### Example Usage
- **Adding a Book**: Enter the book's title, ID, and author when prompted. The book will be added to both the `books` and `available_books` tables.
- **Issuing a Book**: Enter the student’s name and admin number. If the student has no outstanding fines, you can issue the book by providing its ID.
- **Returning a Book**: Provide the book ID and student details to return the book. Fines will be automatically calculated based on the return date.

## Future Enhancements
- Implement an intuitive graphical user interface (GUI) for easier operation.
- Add functionality to generate reports of issued and returned books.
- Enable email notifications for overdue books.
- Allow exporting data to CSV or PDF formats for better management.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Contributing
Contributions are welcome! Please submit a pull request or raise an issue if you have any suggestions or improvements.

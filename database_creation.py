import mysql.connector

a = mysql.connector.connect(host='localhost', user='root', password='iplab', database='librarymanagment_system')
b = a.cursor()

b.execute("create table books(BOOK_NAME VARCHAR(50), BOOK_ID VARCHAR(7), AUTHOR VARCHAR(50))")
b.execute("create table available_books(BOOK_NAME VARCHAR(50), BOOK_ID VARCHAR(7), AUTHOR VARCHAR(50))")
b.execute("create table issue(NAME VARCHAR(50), ADMIN_NO INT, BOOK_ID INT, ISSUE DATE)")
b.execute("create table submit(NAME VARCHAR(50), ADMIN_NO INT, BOOK_ID INT, SUBMIT_DATE DATE)")
b.execute("create table students(NAME VARCHAR(50), ADMIN_NO INT PRIMARY KEY NOT NULL, FINE_AMOUNT INT DEFAULT 0)")
b.execute("create table books_to_be_submitted(NAME VARCHAR(50), ADMIN_NO INT, BOOK_ID INT, SUBMIT_DATE DATE)")

a.commit()
print("tables created")

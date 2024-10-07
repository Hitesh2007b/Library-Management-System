import pandas as pd
import mysql.connector
import datetime
from datetime import date

a = mysql.connector.connect(host='localhost', user='root', password='h1tesh', database='library_managment_system')
b = a.cursor()

# sign up page for students
def signup():
    name = input("enter students name:")
    adminno = int(input("enter admin no:"))
    mysql = 'select exists(select * from students where admin=%s or name=%s)'
    data = (adminno, name)
    b.execute(mysql, data)
    p = b.fetchone()
    z = p[0]
    if z == 1:
        print("already signed up, you can continue")
        main()
    if z == 0:
        h = "insert into students values(%s,%s,0)"
        data = (name, adminno)
        b.execute(h, data)
        a.commit()
        print("*****signed in successfully****")
        print("")
        print("")
        main()

# add a new book
def addbook():
    bookname = input("Enter book title: ")
    bookid1 = input("Enter book id: ")
    bookid = bookid1.split()
    mysql3 = "select exists(select * from books where book_id=%s)"
    b.execute(mysql3, bookid)
    m = b.fetchone()
    z = m[0]
    if z == 0:
        author = input("Enter the author: ")
        data = (bookname, bookid1, author)
        mysql = 'insert into books values(%s,%s,%s)'
        b.execute(mysql, data)
        mysql1 = 'insert into available_books values(%s,%s,%s)'
        b.execute(mysql1, data)
        a.commit()
        print("*****BOOK ADDED SUCCESSFULLY******")
        print(' ')
        print(' ')
    else:
        print("book id already exist, select a different book id")
        addbook()
    main()

# issue a book
def issuebook():
    name = input("enter name:")
    admin = input("enter admin number:")
    mysql = 'select exists(select * from students where admin=%s and name=%s)'
    data = (admin, name)
    b.execute(mysql, data)
    i = b.fetchone()
    o = i[0]
    if o == 1:
        admin1 = admin.split()
        mysql3 = "select fine_amount from students where admin=%s;"
        b.execute(mysql3, admin1)
        j1 = b.fetchone()
        j = j1[0]
        if j > 0:
            print("please submit the book and pay the fine amount, to further take a book")
        else:
            bookid = input("Enter Book_Id:")
            datax = bookid.split()
            mysql = 'select exists(select * from available_books where book_id=%s)'
            b.execute(mysql, datax)
            g = b.fetchone()
            z = g[0]
            if z == 1:
                issue_date = date.today()
                data = (name, admin, bookid, issue_date)
                mysql = 'insert into issue values(%s,%s,%s,%s)'
                submit_date = issue_date + datetime.timedelta(days=7)
                data1 = (name, admin, bookid, submit_date)
                mysql1 = 'insert into books_to_be_submitted values(%s,%s,%s,%s)'
                b.execute(mysql, data)
                b.execute(mysql1, data1)
                a.commit()
                daysdelay = (date.today() - submit_date).days
                fine = daysdelay * 10
                o = "delete from available_books where book_id=%s"
                datay = bookid.split()
                b.execute(o, datay)
                a.commit()
                print("*****BOOK ISSUED TO: ", name)
                print(' ')
                if fine > 0:
                    mysql2 = "update students set fine_amount=fine_amount+%s where admin=%s"
                    data2 = (fine, admin)
                    b.execute(mysql2, data2)
                    a.commit()
                else:
                    fine = 0
                    mysql2 = "update students set fine_amount=%s where admin=%s"
                    data2 = (fine, admin)
                    b.execute(mysql2, data2)
                    a.commit()
            else:
                print("book not available\n")
                print(' ')
        main()
    else:
        print("please sign up first")
        main()

# submit a book
def submitbook():
    name = input("enter name:")
    admin_no = input("Enter Admin_Number: ")
    book_id = input("Enter Book_Id: ")
    submit_date = date.today()
    datax = [book_id]
    mysql = 'select exists(select * from books_to_be_submitted where book_id=%s)'
    b.execute(mysql, datax)
    p = b.fetchone()
    z = p[0]
    if z == 1:
        admin1 = admin_no.split()
        mysql3 = "select fine_amount from students where admin=%s;"
        b.execute(mysql3, admin1)
        j1 = b.fetchone()
        j = j1[0]
        if j > 0:
            print("please submit the book and pay the fine amount, to further take a book")
        else:
            data = (name, admin_no, book_id, submit_date)
            mysql = 'insert into submit values(%s,%s,%s,%s)'
            b.execute(mysql, data)
            ydata = book_id.split()
            locate = 'select * from books where book_id=%s'
            z = b.execute(locate, ydata)
            result = b.fetchall()
            print(result)
            zdata = result[0]
            bookname = zdata[0]
            bookid = zdata[1]
            author = zdata[2]
            data7 = (bookname, bookid, author)
            mysql1 = 'insert into available_books values(%s,%s,%s)'
            b.execute(mysql1, data7)
            mysql2 = "delete from books_to_be_submitted where book_id=%s"
            b.execute(mysql2, ydata)
            a.commit()
            print("*****BOOK SUBMITTED BY: ", name)
            main()
    else:
        print("BOOK NOT ISSUED BY LIBRARY, SUBMIT BOOKS ONLY ISSUED BY THE LIBRARY")
        print(' ')
        main()

# delete a book
def deletebook():
    book_id = input("Enter the book id which is to be deleted: ")
    j = book_id.split()
    delete = "delete from books where book_id=%s"
    delete1 = "delete from available_books where book_id=%s"
    b.execute(delete, j)
    b.execute(delete1, j)
    a.commit()
    print("****BOOK DELETED SUCCESSFULLY*****")
    print(' ')
    main()

# search for a book
def searchbook():
    print('*******************search for a book********************\n')
    que = input("do you know the book_id (y/n): ")
    if que == 'y':
        book_id = input('Enter the book_id:')
        f = book_id.split()
        b.execute('select * from books where book_id=%s', f)
        result = b.fetchall()
        f = pd.DataFrame(result)
        f.columns = ['BOOK TITLE', 'BOOKID', 'AUTHOR']
        print(f)
        print(' ')
    else:
        book_name = input('enter the first letter of book_title:')
        l = book_name + '%'
        n = l.split()
        b.execute("select* from books where book_name like %s", n)
        result = b.fetchall()
        f = pd.DataFrame(result)
        f.columns = ['BOOK TITLE', 'BOOKID', 'AUTHOR']
        print(f)
        print(' ')
    main()

# display books
def displaybook():
    que = int(input("enter 1 to see all books/enter 2 to see available book:"))
    if que == 1:
        print("*****************BOOKS IN LIBRARY***************")
        b.execute("select * from books order by book_id")
        result = b.fetchall()
        f = pd.DataFrame(result)
        f.columns = ['BOOK TITLE', 'BOOKID', 'AUTHOR']
        print(f)
        print(' ')
    elif que == 2:
        print("***************AVAILABLE BOOKS IN LIBRARY*************")
        b.execute("select * from available_books order by book_id")
        result = b.fetchall()
        f = pd.DataFrame(result)
        f.columns = ['BOOK TITLE', 'BOOKID', 'AUTHOR']
        print(f)
        print(' ')
    else:
        print("****************error select whether 1 or 2******************\n")
    main()

# main menu
def main():
    print('*******************************LIBRARY MANAGER**************************\n0.sign up\n1.Add Book\n2.Issue Book\n3.Submit Book\n4.Delete Books\n5.Display Books\n6.search_books\n7.issuedbooks\n8.submittedbooks\n9.books issued to a student\n10.books_to_be_submitted\n11.fine payment\n12.details_of_signed_students\n13.exit ')
    task = input("Enter Task No:")
    if task == '0': signup()
    elif task == '1': addbook()
    elif task == '2': issuebook()
    elif task == '3': submitbook()
    elif task == '4': deletebook()
    elif task == '5': displaybook()
    elif task == '6': searchbook()
    elif task == '7': issuedbooks()
    elif task == '8': submittedbooks()
    elif task == '9': books_issued_to_a_student()
    elif task == '10': books_to_be_submitted()
    elif task == '11': fine_payment()
    elif task == '12': details_of_signed_students()
    elif task == '13': print("thank you and visit again")
    else: print("wrong choice. .. re-enter the task no")
    main()

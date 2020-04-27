import sys
from collections import namedtuple

def SaveBook(book):
    f = open("BookData.csv","a+")
    f.write(book[0] + ',' + book[1] + ',' + book[2] + ',' + book[3])
    f.close()

def AddBook():
    Book = namedtuple("Book", "ID Title Author ISBN")
    id = input("Enter the ID: ")
    title = input("Enter title of book: ")
    author = input("Enter name of author: ")
    isbn = input("Enter ISBN: ")
    newBook = Book(id, title, author, isbn)
    SaveBook(newBook)
    print("Book was added successfullly")

#AddBook()

def GetRecord(input_id):
    with open("BookData.csv","r") as f:
         for line in f:
             line = line.rstrip()
             id,title,author,isbn = line.split(",")
             if (id == input_id):
                 return line

def DisplayBook():
    input_id = input("Enter the ID of book to display: ")
    id,title,author,isbn = GetRecord(input_id).split(",")
    if (id == input_id):
        print('{0: <5}'.format(id) + '{0: <35}'.format(title) + '{0: <25}'.format(author) + '{0: <15}'.format(isbn))


DisplayBook()
import pickle
from datetime import datetime


class Book:
    ISBN: int
    name: str
    author: str
    publisher: str
    publish_date: datetime.date

    def __init__(self, ISBN, name, author, publisher, publish_date):
        self.ISBN = ISBN
        self.name = name
        self.author = author
        self.publisher = publisher
        self.publish_date = publish_date

    def __repr__(self):
        return f'<<{self.ISBN}: {self.name} , {self.author} , {self.publisher} , {self.publish_date}>>'


with open('book.pkl', 'rb') as f:
    books = pickle.load(f)
print(books)

for i in books:
    # i.

    print(i)






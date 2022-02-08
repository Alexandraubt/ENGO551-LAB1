import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

with open("books.csv", "r") as books_file:
    books = csv.DictReader(books_file, delimiter=',')
    for book in books:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)", {"isbn": book["isbn"], "title": book["title"], "author": book["author"], "year": book["year"]})
    db.commit()

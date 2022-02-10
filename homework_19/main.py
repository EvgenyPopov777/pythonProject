from  sqlalchemy.orm import (
Session as SessionType,
scoped_session,
sessionmaker,
)
from models.author import Author
from models.book import Book
from models.base import engine

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def create_book(session: SessionType,Name_books:str)-> Book:
    """""
    :param session:
    :param Name_books:
    :return:
    """""
    book = Book(Name_books=Name_books)
    print("crate book", book)
    session.add(book)
    session.commit()
    print("saved book", book)
    return book
def main():
    """""
    :return:
    """""
session = Session()
create_book(session, "Thomas More.Utopia")
create_book(session, "The Art of War")
create_book(session, "What do women want")


def create_author(session: SessionType,Name_author:str)-> Book:
    """""
    :param session:
    :param Name_author:
    :return:
    """""
    author = Author(Name_author=Name_author)
    print("crate author", author)
    session.add(author)
    session.commit()
    print("saved author", author)
    return author
def main():
    """""
    :return:
    """""
session = Session()
create_author(session, "Author number one")
create_author(session, "Author number two")


if __name__=='main':
    main()

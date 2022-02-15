from sqlalchemy.orm import (
    Session as SessionType,
    scoped_session,
    sessionmaker,
)
from models.author import Author
from models.book import Book
from models.base import engine

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def create_author(session: SessionType, Name_author: str) -> Author:
    """
    :param session:
    :param Name_author:
    :return:
    """
    author = Author(Name_author=Name_author)
    print("create author", author)
    session.add(author)
    session.commit()
    print("saved author", author)
    return author


def create_book(session: SessionType, Name_books: str, author_id: int) -> Book:
    """""
    :param session:
    :param Name_books:
    :param author_id:
    :return:
    """""
    book = Book(Name_books=Name_books, author_id=author_id)
    print("create book", book)
    session.add(book)
    session.commit()
    print("saved book", book)
    return book


def main():
    """
    :return:
    """
    session = Session()
    create_author(session, "Author number one")
    create_author(session, "Author number two")
    create_book(session, "Thomas More.Utopia",1)
    create_book(session, "The Art of War",1)
    create_book(session, "Art and Beauty in Medieval Aesthetics", 1)
    create_book(session, "What do women want",2)

if __name__ == '__main__':
    main()


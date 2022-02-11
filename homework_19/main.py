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


def create_author_and_posts(
        session:SessionType,
        *Name_books:str,
)-> list[Book]:
    """""
    :param session:
    :param Name_books:
    :return:
    """""
    author = session.query(Author)
    for Name_books in Name_books:
        book = Book(author=author)
        print("create book",book)
        session.add(book)
    session.commit()
    print("author's books", author.books)
    return author.books

def main():
    """""
        :return
    """""
    session:SessionType= Session()

    create_author_and_posts(
        session,
        "Author number one",
        "Thomas More.Utopia",
        "The Art of War"
    )
    create_author_and_posts(
        session,
        "Author number two",
        "What do women want"
    )
    session.close()

if __name__=='main':
    main()









# def create_author(session: SessionType,Name_author:str)-> Book:
#     """""
#     :param session:
#     :param Name_author:
#     :return:
#     """""
#     author = Author(Name_author=Name_author)
#     print("create author", author)
#     session.add(author)
#     session.commit()
#     print("saved author", author)
#     return author
#
#
# def create_book(session: SessionType, Name_books:str)-> Book:
#     """""
#     :param session:
#     :param Name_books:
#     :param author_id:
#     :return:
#     """""
#     book = Book(Name_books=Name_books)
#     print("create book", book)
#     session.add(book)
#     session.commit()
#     print("saved book", book)
#     return book
# def main():
#     """""
#     :return:
#     """""
# session = Session()
#
# session: SessionType = Session()
# aut_one=create_author(session,"aut_one")
# another_author_one =session.get(Author,aut_one.id)
# print("another_author_one",another_author_one)
# aut_two=create_author(session,"aut_two")
# another_author_two =session.get(Author,aut_two.id)
# print("another_author_two",another_author_two)

# session = Session()
# create_author(session, "Author number one")
# create_author(session, "Author number two")
#
# create_book(session, "Thomas More.Utopia")
# create_book(session, "The Art of War")
# create_book(session, "What do women want")






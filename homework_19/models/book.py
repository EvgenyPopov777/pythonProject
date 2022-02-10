from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .base import Base
class Book(Base):
    # __tablename__ = "books"
    # id = Column(Integer, primary_key=True)
    Name_books = Column(String(100), unique=True)
    author = relationship("Author", back_populates ="book")
    def  __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"Name_books={self.Name_books!r},"
        )
    def __repr__(self):
        return  str(self)

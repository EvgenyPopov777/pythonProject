from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
class Book(Base):
    Name_books = Column(String(100), unique=False, nullable=False)
    author_id = Column(Integer, ForeignKey("blog_authors.id"), nullable=False)

    author = relationship("Author", back_populates="books")
    def  __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"Name_books={self.Name_books!r},"
            f"author_id={self.author_id}"
        )
    def __repr__(self):
        return str(self)

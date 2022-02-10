from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
class Author(Base):
   # __tablename__ = "authors"
    # id = Column(Integer, primary_key=True)
    Name_author = Column(String(150), unique=True)
    book_id = Column(Integer, ForeignKey("blog_books.id"), nullable=False)
    book = relationship("Book", back_populates="author")
    def  __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"Name_author={self.Name_author!r},"
            f"book_id={self.book_id}"
        )
    def __repr__(self):
        return  str(self)

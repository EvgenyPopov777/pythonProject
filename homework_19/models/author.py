from sqlalchemy import Column, Integer, String, Boolean
from .base import Base
class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    Name_author = Column(String(150), unique=True)
    def  __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"Name_books={self.Name_author!r},"
        )
    def __repr__(self):
        return  str(self)

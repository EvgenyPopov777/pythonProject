from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .base import Base
class Author(Base):
    Name_author = Column(String(150), unique=True)
    books = relationship("Book", back_populates="author")
    def  __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"Name_author={self.Name_author!r},"
        )
    def __repr__(self):
        return  str(self)

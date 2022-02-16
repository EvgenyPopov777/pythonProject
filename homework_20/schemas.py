from pydantic import BaseModel


class BaseSchema(BaseModel):
    id: int

    class Config:
        orm_mode = True


class AuthorSchema(BaseSchema):
    Name_author: str


class BookSchema(BaseModel):
    Name_books: str
    author_id: int

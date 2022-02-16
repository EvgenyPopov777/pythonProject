from typing import List, Dict, Any
import falcon
from falcon import Request, Response
from sqlalchemy.orm import joinedload
from models import Author
from schemas import AuthorSchema


class AuthorsListResource:
    def on_get(self, req: Request, res: Response):
        authors: list[Author] = (
            req.context.session
                .query(Author)
                .options(joinedload(Author.books))
                .all()
        )
        result = [
            AuthorSchema.from_orm(author).dict()
            for author in authors
        ]
        res.media = result


class AuthorDetailsResource:
    def on_get(self, req: Request, res: Response, author_id: str):
        author: Author = (
            req.context.session
                .get(
                Author,
                author_id,
                options=(
                    joinedload(Author.books),
                )
            )
        )
        if author in None:
            res.status = falcon.HTTP_404
            result = {"message": f"author #{author_id} not found"}
        else:
            result = AuthorSchema.from_orm(author).dict()

        res.media = result

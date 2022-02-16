import falcon_sqla
from falcon import App
from authors_views import AuthorsListResource, AuthorDetailsResource
from models.base import engine

manager = falcon_sqla.Manager(engine)
middlewares = {
    manager.middleware,
}
app = App(middleware=middlewares)
authors_list = AuthorsListResource
authors_details = AuthorDetailsResource
app.add_route("/authors", authors_list)
app.add_route("/authors/{author_id}", authors_details)


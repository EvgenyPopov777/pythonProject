from falcon import App, CORSMiddleware
from logging_middleware import  LoggingMiddleware
from  timing_middleware import  TimingMiddleware

from book_views import BooksListResourse,BooksDetailsResourse

ALLOW_ORIGINS = [
    "abc.com",
    "www.google.com",
    "http://httpbin.org"
]
cors = CORSMiddleware(allow_origins = ALLOW_ORIGINS)
middlewares =[
    LoggingMiddleware(),
    TimingMiddleware(),
    cors,
]
books_list = BooksListResourse()
books_details = BooksDetailsResourse()
app = App(middleware = middlewares)
app.add_route("/books",books_list)
app.add_route("/books/{book_id}",books_details)
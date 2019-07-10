from web.url import Url
from web.application import Application


urls = [
    Url('/about', None),
    Url('/api/test/id<int>/question/id<int>', None),
    Url('/', None),
    Url('/api/test/id<int>/question/id<int>/create', None)
]


app = Application(urls, None)
app.configure()


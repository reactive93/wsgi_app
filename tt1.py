from web.url import Url
from web.application import Application


urls = [
    Url('/', None),
    Url('/about', None),
    Url('/api/test/id<int>/question/id<int>', None),
    Url('/api/test/id<int>/question/id<int>/create', None)
]


app = Application(urls, None)
app.configure()


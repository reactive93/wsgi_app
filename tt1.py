from web.url import Url
from web.application import Application


urls = [
    Url('/api/test/id<int>/question/id<int>', 'handler q 1'),
    Url('/', 'index'),
    Url('/about', 'handler about'),
    Url('/api/test/id<int>/question/id<int>/create', 'handler q create'),
    Url('/api/test/name<str>/question/id<int>/create', 'handler q create'),
    Url('/api/test/list/question/id<int>/create', 'handler list q create'),
]


app = Application(urls, None)
app.configure()

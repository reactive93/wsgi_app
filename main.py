import waitress
import os

from web.application import Application

BASE_DIR = os.path.dirname(__file__)

index = os.path.join(BASE_DIR, 'static/html/index.html')
about = os.path.join(BASE_DIR, 'static/html/about.html')

urls = [
    Url('/', IndexHandler('GET', index)),
    Url('/about', AboutHandler('GET', about)),
    Url('/api/test/id<int>/question/id<int>', ParamsHandler('GET', about)),
    Url('/api/test/id<int>/question/id<int>/create', PostHandler('POST', about))
]

config = {
    'base': BASE_DIR,
    'static':'static'
}

app = Application(urls, config)

waitress.serve(app.work, port=8080)
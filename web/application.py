from typing import List
from url import Url
from dispatcher import Dispatcher

class Application:

    def __init__(self,urls:List[Url],config:dict):
        self.config = config
        self.urls = urls

    def configure(self):
        pass
        


    def work(self, environ, start_response_fn):
        """Simplest possible application object"""
        # status = '200 OK'
        # response_headers = [('Content-type', 'text/plain')]
        # start_response(status, response_headers)
        print(environ)
        dispatcher = Dispatcher(environ, start_response_fn)
        status = dispatcher.get_response().get_status()
        headers = dispatcher.get_response().get_headers()
        data = dispatcher.get_response().get_data()
        start_response_fn(status, headers)
        return [data]

from io import BytesIO
from midleware import MidleWare
from base_handler import BaseHandler
class RequestWrapper:

    def __init__(self, request_method:str, path:str, query_path:str, post_fn):
        self.request_method = request_method
        self.path = path
        self.query_path = query_path
        self.post_fn = post_fn
        self.handler = None #type:BaseHandler
        self.post_data = None

        pass
    

class Dispatcher:

    def __init__(self, environ:dict, start_response_fn):

        self.environ = environ
        

        pass

    def parse_query(self, raw_data:str):
        pass

    def parse_post_data(self, raw_data):
        pass

    def read_post(self,method:str,post_fn):
        if method.lower() == 'post':
            raw_data = post_fn().read()
            return self.parse_post_data(raw_data)
        return ''


    def read_query_url(self, query_path:str):
        if query_path != '':
            return self.parse_query(query_path)
        
        return query_path
    
    def get_request_wrapper(self):
        
        method = self.environ['REQUEST_METHOD']
        path = self.environ['PATH_INFO']
        query_path = self.environ['QUERY_STRING']
        post_fn = self.environ['wsgi.input']

        parsed_query_path = self.read_query_url(query_path)
        parsed_query_path = self.read_post(method,post_fn)

        requestWrapper = RequestWrapper(method, path, query_path, post_fn)

        return requestWrapper

    def get_handler(self):
        pass

    def get_response(self):
        wrapperRequest = self.get_handler()
        midleWare = MidleWare(wrapperRequest)

        return midleWare.get_response()
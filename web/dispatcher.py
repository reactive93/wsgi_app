from typing import List
from io import BytesIO
from .midleware import MidleWare
from .base_handler import BaseHandler
from .parser import ParserUrl,UrlTree
class RequestWrapper:

    def __init__(self, request_method:str, path:str, query:dict, post_data:dict):
        self.request_method = request_method
        self.path = path
        self.query = query
        self.handler = None #type:BaseHandler
        self.post_data = post_data
        
        pass
    

class Dispatcher:

    def __init__(self, environ:dict, start_response_fn, tree:UrlTree):

        self.environ = environ
        self.tree = tree
        self.parser_url = ParserUrl()
        pass

    def parse_query(self, raw_data:str)->dict:
        return {}

    def parse_post_data(self, raw_data)->dict:
        return {}

    def read_post(self, method:str, post_fn:BytesIO):
        if method.lower() == 'post':
            raw_data = post_fn.read()
            return self.parse_post_data(raw_data)
        return {}


    def read_query_url(self, query_path:str):
        if query_path != '':
            return self.parse_query(query_path)
        
        return {}
    
    def get_request_wrapper(self):
        
        method = self.environ['REQUEST_METHOD']
        path = self.environ['PATH_INFO']
        query_path = self.environ['QUERY_STRING']
        post_fn = self.environ['wsgi.input']

        
        parsed_query_path = self.read_query_url(query_path)

        parsed_post_data = self.read_post(method,post_fn)

        requestWrapper = RequestWrapper(method, path, parsed_query_path, parsed_post_data)

        return requestWrapper

    def path_exist(self, array:List[UrlTree], part:str, pos:int):
        for i, url_tree in enumerate(array):
            if part == url_tree.part_path:
                return url_tree
            if url_tree.position == pos:
                return url_tree
        return None

    def find_handler(self, main_tree:UrlTree, path:str):
        
        array_path = path.split('/')
        del array_path[0]
        for j, part in enumerate(array_path):
            if part == '':
                return main_tree.handler

            else:
                part_tree = self.path_exist(main_tree.array_item_url, part, j)
                if part_tree is None:
                    return None
                    
                if j == len(array_path)-1:
                    return main_tree.handler
                else:
                    main_tree = part_tree
        

    def get_handler(self):
        requestWrapper = self.get_request_wrapper()

        tree_path = self.parser_url.parse_url(requestWrapper.path)


        

        pass

    def get_response(self):
        wrapperRequest = self.get_handler()
        midleWare = MidleWare(wrapperRequest)

        return midleWare.get_response()
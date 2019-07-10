from typing import List, Set
from .url import Url, ParamUrl
from .dispatcher import Dispatcher

class UrlItem:
    
    def __init__(self,part_path:str,is_static:bool):
        self.part_path = part_path
        self.is_static = is_static


class UrlTree:

    def __init__(self):
        self.part_path= None #type:UrlItem
        self.array_item_url = [] #type: List[UrlTree]
        self.handler = None
        pass

class Application:

    def __init__(self, urls:List[Url], config:dict):
        self.config = config
        self.urls = urls
        self.tree = UrlTree()

    def configure(self):
        self.parse_url()
        pass
    
    def parse_dynamic_url(self, path:str):
        
        for i,item in enumerate(self.split_url):
            if '<' in item:
                if '<' in item and '>' in item:
                    prepare_item = item.replace('>','',len(item)-1)
                    name_type_list_param = prepare_item.rsplit('<')
                    paramUrl = ParamUrl(name_type_list_param[0],name_type_list_param[1],i)
                    return paramUrl

                
                else:
                    raise Exception('Can not parse path ---> '+ path)

    def parse_url(self):
        
        for i, url in enumerate(self.urls):
            current_tree = self.tree
            path_arr = url.path.rsplit('/')
            for j, part in enumerate(path_arr):
                
                if part in current_tree.array_item_url[j].part_path:
                    

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
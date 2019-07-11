from typing import List, Set
from .url import Url, ParamUrl
from .dispatcher import Dispatcher
import queue
class UrlItem:
    
    def __init__(self,part_path:str,is_static:bool):
        self.part_path = part_path
        self.is_static = is_static


class UrlTree:

    def __init__(self):
        self.part_path= '/'
        self.array_item_url = [] #type: List[UrlTree]
        self.handler = None
        self.name_param = None
        self.type = None
        self.position = None
        self.is_dynamic=False
        pass

class Application:

    def __init__(self, urls:List[Url], config:dict):
        self.config = config
        self.urls = urls
        self.tree = UrlTree()

    def configure(self):
        self.parse_url()
        pass
    
    def parse_dynamic_url(self, path:str, pos:int):
        

        if '<' in path and '>' in path:
            prepare_item = path.replace('>','',len(path)-1)
            name_type_list_param = prepare_item.rsplit('<')
            # paramUrl = ParamUrl(name_type_list_param[0],name_type_list_param[1], pos)
            paramUrl = UrlTree()
            paramUrl.name_param = name_type_list_param[0]
            paramUrl.type = name_type_list_param[1]
            paramUrl.position = pos
            paramUrl.is_dynamic = True
            return paramUrl

        
        else:
            raise Exception('Can not parse path ---> '+ path)

    def path_exist(self,array:List[UrlTree], part:str):
        for i, url_tree in enumerate(array):
            if part == url_tree.part_path:
                return url_tree
        return None

    def get_dynamic_part_url(self, arr:List[UrlTree], current_dynamic:UrlTree):
        temp_url = None #type:UrlTree
        for url in arr:
            if url.is_dynamic:
                temp_url = url
                break
        if temp_url.type == current_dynamic.type:
            return temp_url
        
        return None
        

    def parse_url(self):
        
        for i, url in enumerate(self.urls):
            current_tree = self.tree
            path_arr = url.path.split('/') 
            del path_arr[0]

            for j, part in enumerate(path_arr):
                if part == '':
                    current_tree.handler = url.handler
                    continue
                if '<' in part:
                    dynamic = self.parse_dynamic_url(part, j)
                    if j == len(path_arr)-1:
                        dynamic.handler = url.handler
                    if len(current_tree.array_item_url) > 0:
                        exist_dynamic = self.get_dynamic_part_url(current_tree.array_item_url, dynamic)
                        if exist_dynamic:
                            current_tree = exist_dynamic
                            continue
                    current_tree.array_item_url.append(dynamic)
                    current_tree = dynamic
                    continue
                else:
                    part_tree = self.path_exist(current_tree.array_item_url, part)
                    if part_tree is None:
                        new_part = UrlTree()
                        new_part.part_path = part
                        if j == len(path_arr)-1:
                            new_part.handler = url.handler
                        current_tree.array_item_url.append(new_part)
                        current_tree = new_part
                    else:
                        current_tree = part_tree


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
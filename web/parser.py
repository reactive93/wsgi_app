from url import Url

class UrlTree:

    def __init__(self):
        self.array_item_url = []
        self.handler = None
        pass

class ParamUrl:
    def __init__(self, name_param:str, type:str, position:int):
        self.name_param = name_param
        self.type = type
        self.position = position
        pass

class ParserUrl:

    def __init__(self):
        pass
    
    def create_url_tree(self, url:Url):
        path_arr = url.path.rsplit("/")
        urlTree = UrlTree()
        for i, item in enumerate(path_arr):
            if '<' in item:
                if '<' in item and '>' in item:
                    prepare_item = item.replace('>','',len(item)-1)
                    name_type_list_param = prepare_item.rsplit('<')
                    paramUrl = ParamUrl(name_type_list_param[0],name_type_list_param[1],i)
                else:
                    raise Exception('Can not parse path ---> '+ url.path)
            else:

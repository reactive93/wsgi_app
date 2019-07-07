from typing import List

from base_handler import BaseHandler

class ParamUrl:
    def __init__(self,name_param:str,type:str ,position:int):
        self.name_param = name_param
        self.type = type
        self.position = position
        pass

class Url:

    def __init__(self, path:str, handler:BaseHandler):
        self.path = path
        self.handler = handler
        self.paramsUrl = [] #type: List[ParamUrl]
        self.split_url = None #type:List[str]
        self.parse_url(path)

    def parse_url(self, path:str):

        self.split_url = path.rsplit('/')
        
        for i,item in enumerate(self.split_url):
            if '<' in item:
                if '<' in item and '>' in item:
                    prepare_item = item.replace('>','',len(item)-1)
                    name_type_list_param = prepare_item.rsplit('<')
                    paramUrl = ParamUrl(name_type_list_param[0],name_type_list_param[1],i)
                    self.paramsUrl.append(paramUrl)

                
                else:
                    raise Exception('Can not parse path ---> '+ path)


        pass

url = Url('/api/test/id<int>/question/id<int>',None)
url = Url('/api/test/id<int>/question/',None)
url = Url('/api/test/question/',None)
from typing import List


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


class ParserUrl:

    def __init__(self):
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
        

    def parse_url(self, path:str):
        
        
        current_tree = UrlTree()
        root = current_tree
        path_arr = path.split('/') 
        del path_arr[0]

        for j, part in enumerate(path_arr):

            if '<' in part:
                dynamic = self.parse_dynamic_url(part, j)
                current_tree.array_item_url.append(dynamic)
                current_tree = dynamic
                continue
            else:
                new_part = UrlTree()
                new_part.part_path = part
                current_tree.array_item_url.append(new_part)
                current_tree = new_part
        return root


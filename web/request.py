class Request:

    def __init__(self, method:str, path_query:dict, url_params:dict):
        self.method = method
        self.path_query = path_query
        self.url_params = url_params
        pass
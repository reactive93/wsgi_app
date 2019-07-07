
from request import Request

class BaseHandler:


    def __init__(self):
        pass

    def handle(self, request:Request)->str:
        raise NotImplementedError('Method is not implemented')

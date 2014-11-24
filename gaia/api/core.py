class APIManager(object):
    def __init__(self):
        self.func_map = {}

    def register(self,method,func):
        self.func_map[method] = func

    def dispatch(self,method,params):
        func = self.func_map.get(method,None)
        if func:
            data = func(**params)
        else:
            raise Exception("unimplement")
        return data


api_manager = APIManager()

def bind(service):
    def wrapper(func):
        api_manager.register(service,func)
        return func
    return wrapper

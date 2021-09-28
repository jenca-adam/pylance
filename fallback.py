from .error import *
class Fallback:
    def __init__(self,error,message):
        self.error=error
        self.message=message
    def reraise(self):
        raise self.error(self.message)
not_found=Fallback(NotFound,'not found')

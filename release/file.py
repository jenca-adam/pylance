from .digests import Digests
class File:
    def __init__(self,lq):
        self.__dict__.update(lq)
        self.digests=Digest(self.digests)

from .file import *
from pylance.error import *
class Release:
    def __init__(self,rl,version):
        self.files=[File(i)] for i in rl]
        if not self.files:
            raise ReleaseError('no files for release')
        if len(self.files)==1:
            self.__dict__.update(self.files[0])
        else:
            for q in self.files[0].__dict__:
                self.__dict__[q]=[f.__dict__[i] for f in self.files]

        self.version=version

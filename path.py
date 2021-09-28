import os
class Path:
    def __init__(self,path,status=''):
        self.path=path
        self.status=status
def getPath(module):
    if module.__file__ is None:
        if isinstance(module.__path__,list):
            return Path(module.__path__[0])
        return Path(module.__path__._path[0],'(namespace)')
    return Path(module.__file__)
def expand(path):
    if path.endswith('__init__.py'):
        return path.replace('__init__.py','')
    elif path.endswith('__init__'):
        return path.replace('__init__','')

    return path
def strip(fn):
    if fn.endswith('.py'):
         m=fn.replace('.py','').split(os.path.sep)
    m=expand(fn).split(os.path.sep)
    cu=[]
    mx=len(m)
    i=0
    r=[]
    for k in m:
        i+=1
        if i==mx-1:
            r=['/'.join(cu)+'/',k]
            break
        else:
            cu.append(k)

    return r

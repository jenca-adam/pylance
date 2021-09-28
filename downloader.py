from .error import *
import tqdm
from urllib.error import HTTPError as herr
from httplib2 import Http
from urllib.request import urlopen
h=Http('.cache')
def download(url,progress=False,fallback=None):
    if not progress:
        r,c =h.request(url)
    else:
        print(f'Downloading {url!r}')
        try:
            r=urlopen(url)
        except herr:
            if fallback is None:
                raise HTTPNotFound('not found')
            fallback.reraise()

        sz=int(r.headers['Content-Length'])
        res=[]
        for i in tqdm.tqdm(range(sz)):
            res.append(r.read(1))
        c=b''.join(res)
    if r.status!=200:
        if fallback is None:
            raise HTTPNotFound('not found')
        fallback.reraise()
    return c.decode('utf-8')

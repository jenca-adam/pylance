import tarfile
import gzip
import os
from _io import BytesIO
from .downloader import download
from .error import StreamError
from .utils import has_attr
def _check(stream):
    if not has_attr(stream,'read'):
        raise StreamError(
            "stream must have a 'read' attribute"
            )

def _gunzip(stream):
    gzf = gzip.GzipFile(fileobj=stream,mode='rb')
    gzf.seek(0)
    return BytesIO(gzf.read())
def _load(stream):
    if isinstance(stream,bytes):
        stream=BytesIO(stream)
    _check(stream)
    stream=_gunzip(stream)
    tar=tarfile.TarFile(fileobj=stream)
    memb=tar.getmembers()
    return tar,memb
def load(url):
    result=download(url)
    return _load(result)
def splitext(fn):
    if fn.endswith('.tar.gz'):
        return os.path.splitext(os.path.splitext(fn)[0])[0]
    return os.path.splitext(fn)[0]

from pylance.downloader import download
from pylance.error import *
class PyPI:
    SIMPLE='https://pypi.org/simple/{}'
    PROJECT='https://pypi.org/project/{}'
    API='https://pypi.org/pypi/{}/json'
def makeURL(name,t=PyPI.SIMPLE):
    return t.format(name)
def makeProjectURL(name,t=PyPI.PROJECT):
    return t.format(name)
def makeApiURL(name,t=PyPI.API):
    return t.format(name)
def PyPIDownload(name,t=PyPI.API):
    try:
        return download(makeURL(name,t))
    except HTTPNotFound:
        raise NotFound('could not download:not found')
    except HTTPError as e :
        raise PyPIDownloadError(str(e))


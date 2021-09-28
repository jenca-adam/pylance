from pylance.downloader import download
from pylance.versions import Version
from pylance.pypi.simple import Simple
from bs4 import BeautifulSoup as bs
class Collector:
    def __init__(self,url):
        content=download(url,progress=True)
        

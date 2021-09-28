from pylance.downloader import download
from pylance.fallback import not_found
from pylance.metadata import Metadata
from .url import PyPIDownload
def PyPIMeta(name):
    result=PyPIDownload(name)


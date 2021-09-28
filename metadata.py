import os
import re
from bs4 import BeautifulSoup as bs
from .path import *
from .eggdist import *
from .required import *
from .pypi import *
from .entries import *
from .mailto import *
from .wheel import *
class Metadata:pass
def parseMetadata(path):
    dir,pn=strip(path)
    metadir=None
    for fn in os.listdir(dir):
        if fn.startswith(pn) and fn!=pn:
            metadir=os.path.join(dir,fn)
            break
    if metadir is None:
        return {}
    metaf = metadataFile(metadir)

    meta = open(metaf).read()

    return _parseMetadata(meta,metadir)

    
def _parseMetadata(metadata,metadir):
    result={}
    desc=[]
    cmpd=False
    for line in metadata.splitlines():
        try:
            key,val=line.split(': ',1)
            if cmpd and key!="Platform":
                raise ValueError
            if key.lower() in result:
                
                if not isinstance(result[key.lower()],set):
                    result[key.lower()]={result[key.lower()]}
                result[key.lower()].add(val)
            else:
                result[key.lower()]=val
            if key=='Description':
                desc.append(val)
        except:
            desc.append(line)
            cmpd=True
    result['description']='\n'.join(desc)
    result=parse_requirements(result,metadir)
    return result

def PyPIMeta(name):
    metadata={}
    content=PyPIDownload(name,t=PyPI.PROJECT)
    soup=bs(content,'html.parser')
    q = soup.body.find('h3', text = 'Project links').nextSibling.nextSibling
    metadata['links']=ProjectLinks(q)
    metadata['maintainers']=Maintainers(soup)
    ael = soup.body.find('strong', text = 'Author:').nextSibling.nextSibling
    metadata['author']=ael.text
    metadata['author_email']=split_mailto(ael['href'])
    metadata['classifiers']=Classifiers(soup)
    return metadata

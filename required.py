from .set import set_iterator as iter
from .splitter import first
import os

def parse_requirements(meta,d):
    meta['requires']=[]
    if "requires.txt" in os.listdir(d):
        meta['requires']=open(os.path.join(d,"requires.txt"),"r").read().splitlines()
    if 'requires-dist' in meta:
        g=iter(meta['requires-dist'])
        for a in g:
            meta['requires'].append(first(a,' '))
    return meta

        

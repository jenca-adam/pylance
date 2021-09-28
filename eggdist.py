import os
from .error import *
EGG=0
DIST=1
def getType(dirname):
    ld=os.listdir(dirname)
    if "PKG-INFO" not in ld:
        if "METADATA" not in ld:
            raise MetadataError(
                                f"directory {dirname} could not by identified neither as .egg-info nor .dist-info"
                                )
        return DIST

    return EGG
def metadataFile(dirname):
    Type = getType( dirname )
    if Type == DIST:
        return os.path.join( dirname, "METADATA" )
    elif Type == EGG:
        return os.path.join( dirname, "PKG-INFO" )



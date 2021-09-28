from .error import *
import string
from semver import VersionInfo
import re
version_split=re.compile('(\d+.\d+.\d+)\s?')
class Version(VersionInfo):
    @classmethod
    def fromPackageName(self,pn):
        if '==' in pn:
            return self._parse(self,pn.split('==',1)[1])
        if '-' in pn:
            return self._parse(self,pn.split('-',1)[1])
        else:
            raise VersionError('bad package name')
    def _parse(self,v):
        v=v.replace('0b','').replace('0rc','').replace('0a','').replace('.eta','.')
        if v.endswith(tuple(string.ascii_lowercase)):
            v=v[:-1]
        q=[i.replace('.','') for i in v.split('.')]
        if len(q)>3:
            q=q[:3]
        if len(q)==2:
            q.append('0')
        if len(q)==1:
            q.append('0.0')
        m='.'.join(q)
        m=version_split.search(m).group(1)
        return self.parse(m)
   

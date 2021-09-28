from pylance.versions import Version
from pylance.error import *
from pylace.release import Release
import warnings
from bs4 import BeautifulSoup as bs
class Simple:
    def __init__(self,l,suffix,name='',ignore_warning=False):
        self.links=[ ]
        for q in l:
            if l[q]:
                self.links.append(Release(l[q]))
        if not self.links and not ignore_warning:
            warnings.warn(PackageWarning(
                            f'''Project {suffix} has no links uploaded. This may cause problems when getting metadata. 
                            Metadata can be incomplete. To get rid of this warning, pass argument 'ignore_warning=True'. '''))
        self.versions=[Version._parse(l.version) for l  in self.links]

    def find_latest_version(self):
        return max(self.versions)

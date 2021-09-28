import importlib
import os
import shutil
from .downloader import download
from .error import *
from .path import getPath,expand
from .utils import *
from .metadata import *
from .pypi import *
class Package:
    def __init__(self,name):
        self.name=name
        try:
            self.module=importlib.import_module(name)
            self.path=getPath(self.module).path
            self.installed=True
            self.file=False
            if has_attr(self.module,"__file__") and not self.path.endswith('__init__.py'):
                self.file=True
            self.metadata=parseMetadata(self.path)
        except ImportError:
            self.module=None
            self.installed=False
            self.url=makeURL(name)
            try:
                result=PyPIDownload(name)
            except NotFound:
                raise NotFound(
                            f'package {self.name} is not on PyPI'
                            )
            self.metadata=PyPIMeta(name)
        try:
            self.simple=Simple(name)
        except:
            self.simple=None

    def install(self):
        if self.installed:
            raise AlreadyInstalled
    def uninstall(self):
        try:
            self._uninstall()
        except PermissionError:
            raise PermissionDenied
    def _uninstall(self):
        if not self.installed:
            raise NotInstalled
        if self.file:
            os.remove(self.path)
        else:
            shutil.rmtree(expand(self.path))

        
    def __getattr__(self,attr):
        if not self.metadata:
            raise AttributeError
        return self.metadata[attr]
    def __repr__(self):
        if self.installed:
            return f'<package "{self.name}" from "{getPath(self.module).path}" {getPath(self.module).status}>'
        return f'<package "{self.name}" from {self.url} (uninstalled)>'

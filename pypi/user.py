from dateutil.parser import parse
from bs4 import BeautifulSoup as bs
from pylance.downloader import download
from pylance.error import *
class User:
    def __init__(self,uname):
        self.url=f'https://pypi.org/user/{uname}'
        try:
            res=download(self.url)
        except HTTPError:
            raise UserNotFound('user not found')
        soup=bs(res,'html.parser')
        apel=soup.find(class_="author-profile__name")
        self.name=""
        if apel:
            self.name=apel.text
        self.image_url=soup.select_one('#content > div > div > div.left-layout__sidebar > div > img')['src']
        self.username=uname
        b=soup.select(".package-snippet__title")
        self.projects=[b.text for b in b]
    def __repr__(self):
        if self.name:
            return f'<User {self.username} ({self.name})>'
        return f'<User {self.username}>'
        

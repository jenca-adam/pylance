class ProjectLink:
    def __init__(self,name,url):
        self.name=name.strip()
        self.url=url
    def __repr__(self):
        return f'<ProjectLink [{self.name}] ({self.url})>'
class ProjectLinks:
    def __init__(self,q):
        self.lis=q.findAll('li')
        self.links=[]
        for m in self.lis:
            z=m.a
            url=z['href']
            txt=z.text
            pl=ProjectLink(txt,url)
            self.links.append(pl)
            setattr(self,txt.lower().strip(),pl)
            



class Classifiers:
    def __init__(self,soup):
        q=soup.select('.sidebar-section__classifiers>li')
        self.classifiers={}
        for a in q:
            key=list(a.children)[1].text
            values=a.ul.findAll('li')
            values=[i.text.strip() for i in values]
            self.classifiers[key]=values
    def __getitem__(self,i):
        return self.classifiers[i]


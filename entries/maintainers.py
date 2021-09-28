from pylance.pypi.user import User

class Maintainers:
    def __init__(self,ah):
        ms=set()
        for q in ah.findAll('span',class_="sidebar-section__user-gravatar-text"):
            ms.add(q.text.strip())
        self.maintainers=[User(i) for i in list(ms)]
    def __iter__(self):
        return iter(self.maintainers)
    def __getitem__(self,i):
        return self.maintainers[i]

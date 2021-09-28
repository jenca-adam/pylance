import parse
def split_mailto(mlink):
    return parse.parse('mailto:{l}',mlink)['l']

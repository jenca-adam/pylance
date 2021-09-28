def set_iterator(s):
    if isinstance(s,set):
        return iter(s)
    return {s}

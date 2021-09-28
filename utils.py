def has_attr(a,b):
    if hasattr(a,b):
        if getattr(a,b):
            return True
    return False

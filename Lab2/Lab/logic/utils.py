import inspect

primitives = set(
    [
        int,
        float,
        bool,
        str
    ])
    
def is_basetype(obj: object) -> bool:
    for el in primitives:
        if el.__name__ == obj.__name__:
            return True
    if el in [dict, list, tuple, set]:
        if el.__name__ == obj.__name__:
            return True
    return False


def is_none(_obj):
    return _obj is None

def is_primitive(obj: object) -> bool:
    return type(obj) in primitives

def is_instance_of(obj):
    if not hasattr(obj, '__dict__'):
        return False
    if inspect.isroutine(obj):
        return False
    if inspect.isclass(obj):
        return False
    else:
        return True
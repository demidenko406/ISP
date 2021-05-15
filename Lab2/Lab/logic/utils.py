import inspect

primitives = set(
    [
        int,
        float,
        bool,
        str
    ])

def is_none(_obj):
    return _obj is None

def is_primitive(obj: object) -> bool:
    return type(obj) in primitives

def is_instance_of(obj):
    if not hasattr(obj, '__dict__'):
        return False# pragma: no cover
    if inspect.isroutine(obj):# pragma: no cover
        return False# pragma: no cover
    if inspect.isclass(obj):# pragma: no cover
        return False# pragma: no cover
    else:
        return True
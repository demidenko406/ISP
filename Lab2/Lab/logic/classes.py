import types

def class_to_dict(attr,passed_dict,_mro):
    _dict = {}
    _dict["__name__"] = attr.__name__
    _dict["__mro"] = _mro
    return _dict

def dict_to_class(passed_dict,attrs):
    classes = []
    if passed_dict['__mro'] != 'None':
        for x in passed_dict['__mro'].keys():
            classes.append(passed_dict['__mro'][x])
    mro = []
    mro.extend(classes)
    mro.append(object)
    _class = type(passed_dict["__name__"],tuple(mro),attrs)   
    return _class





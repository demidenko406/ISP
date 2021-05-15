from io import FileIO 
import types
import re
import inspect
import builtins
import Lab.logic.functions as functions
import Lab.logic.classes as classes
from Lab.logic.utils import *
import json

class ToDict():

    def object_to_dict(self,attr,_dict):
        
        if is_none(attr):
            _dict["_type"] = 'none'
            return None

        elif is_primitive(attr):
            _dict["_type"] = 'primitive'    
            return attr

        elif isinstance(attr, types.FunctionType):
            _dict["_type"] = 'func'
            return functions.func_to_dict(attr)

        if type(attr) in [list, set, tuple, dict, frozenset]:
            if isinstance(attr, dict):
                result = {key: self.object_to_dict(attr[key],_dict) for key in attr}
                _dict['_type'] = 'dict'
            elif type(attr) in [frozenset, set, tuple]:
                result = [self.object_to_dict(el,_dict) for el in attr]
                _dict['_type'] =  f"{attr.__class__.__name__}"
            else:
                result = [self.object_to_dict(el,_dict) for el in attr]
                _dict['_type'] = 'list'
            return result

        elif isinstance(attr,types.MappingProxyType):
            _dict["_type"] = '__dict__'
            return _dict['attrs']

        elif isinstance(attr,type):
            _mro = {}
            bases = []
            _dict["_type"] = 'classtype'
            if len(attr.__bases__) == 1:
                _mro = 'None'
            else:
                for _super in attr.__bases__:
                    if _super != object:
                        _mro[_super.__name__] = self.pack_to_dict(_super)
            return classes.class_to_dict(attr,_dict,_mro)

        elif is_instance_of(attr):
            _dict['_type'] = 'instance'
            return self.pack_to_dict(attr.__class__)
        else:
            return None

    def wrap_attrs(self,_object, attrs_dict):
        for attribute in list(_object.__dict__.keys()):
            attrs_dict['attrs'][attribute] = None
        for lower_attribute in attrs_dict['attrs'].keys():
            if(lower_attribute == "__dict__"):
                attrs_dict['attrs'][lower_attribute] = {'attrs': {}, 'decomposed': None,'_type': None}    
                continue
            if(lower_attribute == "mro"):
                continue
            attr = getattr(_object, lower_attribute)
            attrs_dict['attrs'][lower_attribute] = {'attrs': {}, 'decomposed': None,'_type': None}
            if hasattr(attr, "__dict__"):
                self.wrap_attrs(attr, attrs_dict['attrs'][lower_attribute])
            else:
                attrs_dict['attrs'][lower_attribute]['decomposed'] = self.object_to_dict(attr,attrs_dict['attrs'][lower_attribute])
        attrs_dict['decomposed'] = self.object_to_dict(_object,attrs_dict)
        return attrs_dict

    def pack_to_dict(self,_object):
        attribute_dict = {'attrs': {}, 'decomposed': None,'_type' : None}
        if hasattr(_object, "__dict__"):
            attribute_dict = self.wrap_attrs(_object, attribute_dict)
        else:
            attribute_dict['decomposed'] = self.object_to_dict(_object,attribute_dict)
        return attribute_dict

class FromDict():

    def unpack_from_dict(self,dictofobject):
        _dict = {}    
        return self.unwrap(dictofobject,_dict)

    def unwrap(self,_dictionary,unwraped):
        if _dictionary['attrs']:
            for y in _dictionary['attrs'].keys():
                _dec = {}
                unwraped[y] = self.unwrap(_dictionary['attrs'][y],_dec)

        if(_dictionary['_type'] == 'primitive'):
            return _dictionary['decomposed']
        
        if(_dictionary['_type'] == 'list'):
            return _dictionary['decomposed']
            
        elif(_dictionary['_type'] == 'dict'):
            return _dictionary['decomposed']

        elif(_dictionary['_type'] == 'func'):
            func = functions.dict_to_func(_dictionary['decomposed'])
            for y in unwraped.keys():
                setattr(func,y,unwraped[y])
            return func

        elif(_dictionary['_type'] == 'classtype'):
            if _dictionary['decomposed']['__mro'] != 'None':
                for _superclass in _dictionary['decomposed']['__mro'].keys():
                    _dictionary['decomposed']['__mro'][_superclass] = self.unpack_from_dict(_dictionary['decomposed']['__mro'][_superclass])
            cl = classes.dict_to_class(_dictionary['decomposed'], unwraped)
            for y in unwraped.keys():
                if y != '__dict__':
                    setattr(cl,y,unwraped[y])
            return cl

        elif(_dictionary['_type']=='instance'):
            _class = self.unpack_from_dict(_dictionary['decomposed'])
            _inst = _class.__new__(_class)
            for y in unwraped.keys():
                if y != '__dict__':
                    setattr(_inst,y,unwraped[y])
            return _inst





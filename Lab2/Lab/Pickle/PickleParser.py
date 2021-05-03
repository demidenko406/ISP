from logic.dictmaker import *
from pickle import dumps,loads

class PickleParse:
    base_dumps = dumps
    base_loads = loads 

    def dump(self, obj: object, file: object = None, unpacked=True) -> None: 
        if unpacked: 
            unpacker =  ToDict()
            packed_obj = unpacker.pack_to_dict(obj)
        else: 
            packed_obj = obj
        if file:
            with open(file, 'w') as file:
                file.write(PickleParser.base_dumps(packed_obj))
        else: 
            raise ValueError("File transfer aborted")

    def dumps(self, obj: object) -> None: 
        packed_obj = ToDict().pack_to_dict(obj)
        return PickleParser.base_dumps(packed_obj)

    def load(self, file: object, unpack=True) -> Any: 
        if file:
            with open(file, 'r') as file:
                raw_obj = TomlParser.base_loads(file.read())
            if unpack: 
                unpacked_obj = FromDict().unpack_from_dict(raw_obj)
                return unpacked_obj
            else: 
                return raw_obj

        else:
            raise ValueError("File transfer aborted")

    def loads(self, json: str) -> Any: 
        raw_obj = TomlParser.base_loads(json)
        unpacked_obj = FromDict().unpack_from_dict(raw_obj)
        return unpacked_obj
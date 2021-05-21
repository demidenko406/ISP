from io import FileIO 
from typing import Any, IO
from Lab.Json import json_parse as json_
from Lab.logic.dictmaker import *



class JsonParser:
    unpacker = ToDict()
    packer = FromDict()

    def dump(self, obj: object, file: object = None, unpacked=True) -> None: 
        packed_obj = self.unpacker.pack_to_dict(obj)
        if file:
            with open(file, 'w') as file:
                json_.dump(packed_obj,file)
        else: 
            raise ValueError("File transfer aborted")

    def dumps(self, obj: object) -> None:# pragma: no cover 
        packed_obj = self.unpacker.pack_to_dict(obj)
        return json_.dumps(packed_obj)

    def load(self, file: object, unpack=True) -> Any: 
        if file:
            with open(file, 'r') as file:
                raw_obj = json_.load(file)
            unpacked_obj = FromDict().unpack_from_dict(raw_obj)
            return unpacked_obj
        else:
            raise ValueError("File transfer aborted")

    def loads(self, str: str) -> Any: 
        raw_obj = json_.loads(str)
        unpacked_obj = FromDict().unpack_from_dict(raw_obj)
        return unpacked_obj

from typing import Any, IO
import pickle
from Lab.logic.dictmaker import *

class PickleParse:
    unpacker = ToDict()
    packer = FromDict()

    def dump(self, obj: object, file: object = None) -> None: 
        packed_obj = self.unpacker.pack_to_dict(obj)
        if file:
            with open(file, 'wb') as file:
                pickle.dump(packed_obj,file)
        else: 
            raise ValueError("File transfer aborted")

    def dumps(self, obj: object) -> None: 
        packed_obj = unpacker.pack_to_dict(obj)
        return pickle.dumps(packed_obj)

    def load(self, file: object, unpack=True) -> Any: 
        if file:
            with open(file, 'rb') as file:
                return self.packer.unpack_from_dict(pickle.load(file))
        else:
            raise ValueError("File transfer aborted")

    def loads(self, string: str) -> Any:  
        return packer.unpack_from_dict(pickle.loads(string))

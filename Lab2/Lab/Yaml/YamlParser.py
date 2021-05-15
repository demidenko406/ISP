from typing import Any, IO # pragma: no cover
import yaml
from Lab.logic.dictmaker import *

class YamlParse:
    unpacker =  ToDict()
    packer = FromDict()

    def dump(self, obj: object, file: object = None) -> None: 
        packed_obj = self.unpacker.pack_to_dict(obj)
        if file:
            with open(file, 'w') as file:
                file.write(self.dumps(obj))
        else: 
            raise ValueError("File transfer aborted")

    def dumps(self, obj: object) -> None: 
        packed_obj = self.unpacker.pack_to_dict(obj)
        return yaml.dump(packed_obj)

    def load(self, file: object) -> Any: 
        if file:
            with open(file, 'r') as file:
                raw_obj = self.loads(file.read())
            return raw_obj
        else:
            raise ValueError("File transfer aborted")

    def loads(self, yam: str) -> Any: 
        raw_obj = yaml.load(yam)
        unpacked_obj = self.packer.unpack_from_dict(raw_obj)
        return unpacked_obj

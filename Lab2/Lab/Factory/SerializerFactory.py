from Json import JsonParse
from Pickle import PickleParser
from Toml import TomlParser
from Yaml import YamlParser 

class SerializerFactory:
    def __init__(self):
        self._creators = {}

    def create_serializer(self, format, creator):
        self._creators[format.lower()] = creator

    def get_serializer(self, format):
        creator = self._creators.get(format.lower())
        if not creator:
            raise ValueError(format)
        return creator()


factory = SerializerFactory()

factory.create_serializer('JSON', JsonParse.JsonParser)
factory.create_serializer('TOML', TomlParser.TomlParser)
factory.create_serializer('YAML', YamlParser.YamlParse)
factory.create_serializer('PICKLE', PickleParser.PickleParse)
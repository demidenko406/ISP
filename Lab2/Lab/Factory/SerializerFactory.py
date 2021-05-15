from Lab.Json import JsonParse
from Lab.Pickle import PickleParser
from Lab.Yaml import YamlParser 

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
factory.create_serializer('YAML', YamlParser.YamlParse)
factory.create_serializer('PICKLE', PickleParser.PickleParse)

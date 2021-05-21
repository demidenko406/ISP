from Lab.Factory import SerializerFactory

class Serializer:
    def __init__(self, default_form="json"):
        self.form = default_form

    def change_form(self, new_form):
        if self.form == new_form:
            return False
        else:
            self.form = new_form
            return True

    def load(self, fp):
        serializer = SerializerFactory.factory.get_serializer(self.form)
        return serializer.load(fp)

    def loads(self, string):
        serializer = SerializerFactory.factory.get_serializer(self.form)
        return serializer.loads(string)

    def dump(self, obj, fp):
        serializer = SerializerFactory.factory.get_serializer(self.form)
        serializer.dump(obj, fp)

    def dumps(self, obj):
        serializer = SerializerFactory.factory.get_serializer(self.form)
        return serializer.dumps(obj)


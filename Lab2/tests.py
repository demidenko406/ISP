import unittest
from Test_objects import Bottom,bottom_instance,Triangle,list_example,dict_example,lam
from Lab.Json.JsonParse import JsonParser
from Lab.Yaml import YamlParser
from Lab.Pickle import PickleParser
from Lab.Sereializer import Serializer


class TestParsers(unittest.TestCase):
    def setUp(self):

        #self.yaml_parser = YamlParser()
        #self.json_parser = JsonParser()
        #self.pickle_parser = PickleParser()
        self.json_parser = Serializer("json")
        self.yaml_parser = Serializer("yaml")
        self.pickle_parser = Serializer("pickle")

    # Test list
    def test_json_list_dump_load(self):
        self.json_parser.dump(list_example, './Tests/list_example.json')
        obj_to_compare = self.json_parser.load('./Tests/list_example.json')
        self.assertEqual(obj_to_compare, list_example)

    def test_pickle_list_dump_load(self):
        self.pickle_parser.dump(list_example, './Tests/list_example.pickle')
        obj_to_compare = self.pickle_parser.load('./Tests/list_example.pickle')
        self.assertEqual(obj_to_compare, list_example)

    def test_yaml_list_dump_load(self):
        self.json_parser.dump(list_example, './Tests/list_example.yaml')
        obj_to_compare = self.yaml_parser.load('./Tests/list_example.yaml')
        self.assertEqual(obj_to_compare, list_example)

    #dict
    def test_json_dict_dump_load(self):
        self.json_parser.dump(dict_example, './Tests/dict_example.json')
        obj_to_compare = self.json_parser.load('./Tests/dict_example.json')
        self.assertEqual(obj_to_compare, dict_example)

    def test_pickle_dict_dump_load(self):
        self.pickle_parser.dump(dict_example, './Tests/dict_example.pickle')
        obj_to_compare = self.pickle_parser.load('./Tests/dict_example.pickle')
        self.assertEqual(obj_to_compare, dict_example)

    def test_yaml_dict_dump_load(self):
        self.json_parser.dump(dict_example, './Tests/dict_example.yaml')
        obj_to_compare = self.yaml_parser.load('./Tests/dict_example.yaml')
        self.assertEqual(obj_to_compare, dict_example)

    # Test self object dump load
    def test_json_func_dump_load(self):
        self.json_parser.dump(Triangle, './Tests/triangle.json')
        obj_to_compare = self.json_parser.load('./Tests/triangle.json')
        self.assertEqual(obj_to_compare(10,11,12), Triangle(10,11,12))

    def test_pickle_func_dump_load(self):
        self.pickle_parser.dump(Triangle, './Tests/triangle.pickle')
        obj_to_compare = self.pickle_parser.load('./Tests/triangle.pickle')
        self.assertEqual(obj_to_compare(10,11,12), Triangle(10,11,12))

    def test_yaml_func_dump_load(self):
        self.json_parser.dump(Triangle, './Tests/triangle.yaml')
        obj_to_compare = self.yaml_parser.load('./Tests/triangle.yaml')
        self.assertEqual(obj_to_compare(10,11,12), Triangle(10,11,12))


    def test_json_lambda_dump_load(self):
        self.json_parser.dump(lam, './Tests/lam.json')
        obj_to_compare = self.json_parser.load('./Tests/lam.json')
        self.assertEqual(obj_to_compare(2), lam(2))

    def test_pickle_lambda_dump_load(self):
        self.pickle_parser.dump(lam, './Tests/lam.pickle')
        obj_to_compare = self.pickle_parser.load('./Tests/lam.pickle')
        self.assertEqual(obj_to_compare(2), lam(2))

    def test_yaml_lambda_dump_load(self):
        self.yaml_parser.dump(lam, './Tests/lam.yaml')
        obj_to_compare = self.yaml_parser.load('./Tests/lam.yaml')
        self.assertEqual(obj_to_compare(2), lam(2))

    # Test self lambda dump load
    def test_json_class_dump_load(self):
        self.json_parser.dump(Bottom, './Tests/bottom.json')
        obj_to_compare = self.json_parser.load('./Tests/bottom.json')
        inst = obj_to_compare("Try")
        inst2 = Bottom("Try")
        self.assertEqual(inst.value,inst2.value)

    def test_pickle_class_dump_load(self):
        self.pickle_parser.dump(Bottom, './Tests/bottom.pickle')
        obj_to_compare = self.pickle_parser.load('./Tests/bottom.pickle')
        inst = obj_to_compare("Try")
        inst2 = Bottom("Try")
        self.assertEqual(inst.value,inst2.value)

    def test_yaml_class_dump_load(self):
        self.json_parser.dump(Bottom, './Tests/bottom.yaml')
        obj_to_compare = self.yaml_parser.load('./Tests/bottom.yaml')
        inst = obj_to_compare("Try")
        inst2 = Bottom("Try")
        self.assertEqual(inst.value,inst2.value)

    #instance
    def test_json_inst_dump_load(self):
        self.json_parser.dump(bottom_instance, './Tests/bottom_inst.json')
        obj_to_compare = self.json_parser.load('./Tests/bottom_inst.json')
        self.assertEqual(obj_to_compare.value,bottom_instance.value)

    def test_pickle_inst_dump_load(self):
        self.pickle_parser.dump(bottom_instance, './Tests/bottom_inst.pickle')
        obj_to_compare = self.pickle_parser.load('./Tests/bottom_inst.pickle')
        self.assertEqual(obj_to_compare.value,bottom_instance.value)

    def test_yaml_inst_dump_load(self):
        self.yaml_parser.dump(bottom_instance, './Tests/bottom_inst.yaml')
        obj_to_compare = self.yaml_parser.load('./Tests/bottom_inst.yaml')
        self.assertEqual(obj_to_compare.value,bottom_instance.value)

if __name__ == "__main__":
    unittest.main()
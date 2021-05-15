class Base():
    def SayHello(self,value):
        print("Hello from Base",value)
    def __init__(self,attr):
        print("init of Base",attr)
        self.attr = attr.upper()
class Middle_One(Base):
    def SayHello(self,value):
        print("Hello from Middle_One",value)
    def __init__(self,attr):
        print("init of Middle_One",attr)
        self.attr = attr.upper()
    value = 200
class Middle_Two(Base):
    def SayGoodbye(self,value):
        print("Goodbye from Middle_two",value)
    def __init__(self,attr):
        print("init of Middle_Two",attr)
        self.attr2 = attr.upper()
        
class Bottom(Middle_One,Middle_Two):
    def __init__(self,attr):
        print("init of MyCLass",attr)
        self.attr = attr.upper()
    
bottom_instance = Bottom("Hello")

def Triangle(x,y,z):
    print(x+y+z)

list_example = [["Hello","Try","Ex"],"draw","triangle"]

dict_example = {"Hy":"Hello","Number":13}

lam = lambda x: x + 1

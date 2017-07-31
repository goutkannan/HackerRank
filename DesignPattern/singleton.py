"""
using __new__ of the object initialization methods to override the __init__s

"""
class Singleton():

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_singleton'):
            cls._singleton = super(Singleton,cls).__new__(cls)
        return cls._singleton

    def __init__(self,val):
        self.banner=val

a = Singleton("A")
b= Singleton("B")
print(b.banner," ...", a.banner)

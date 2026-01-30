from abc import abstractmethod
import typing
class C:

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def print_name(self):
        pass

    @typing.final
    def greeting(self):
        print(f"Hello {self.name}!")


class C1(C):
    #class variable
    class_var = 10

    @staticmethod
    def class_static_method():
        print("Can be called without instantiating a class")

    
    @classmethod
    def class_method(cls):
        print("This is a class method that belongs to all instances of this class")
        print(f"class variable: {cls.class_var}")

    def print_name(self):
        print(f"Name: {self.name}")

C1.class_static_method()

my_class = C1("class 1")

my_class.class_method()

my_class.print_name()
my_class.greeting()

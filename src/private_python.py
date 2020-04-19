

class Test:
    """Private variables in python"""

    def __init__(self):
        self.bar = 11
        self._baz = 24  # _ prefix a name is to be treated as private by the programmer
        # python doesn't have a strong distinction btw private and public variables like java does
        # it's more a hint to another programmer (that a variables carries some internal state)
        # That's not really part of the public interface
        self.__jaz = 44
        # __ there is actually the python iterpreter does. That applies some name mangling
        # That's gonna change the name of that variables in a way that to make harder to create a collision
        # when someone else extends this class
 



class Mapping:
    def __init__(self, iterables):
        self.item_list = []
        self.__update(iterables)

    def update(self, iterable):
        for item in iterable:
            self.item_list.append(item)

    __update = update  # private copy of original update method


class MappingSubClass(Mapping):
    def update(self, key, value):
        for item in zip(key, value):
            self.item_list.append(item)


inst1 = MappingSubClass([54,76,34,81])
print(inst1.item_list)

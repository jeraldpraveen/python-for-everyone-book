stuff = list()
print(dir(stuff))
# The program produces the following output:
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__',
# '__iter__', '__le__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)


an = PartyAnimal()
print("Type", type(an))
an.party()
an.party()
# The program produces the following output:
# Type <class '__main__.PartyAnimal'>
# So far 1
# So far 2

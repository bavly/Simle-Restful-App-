import json
class Foo():
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def __str__(self):
        return json.dumps(self.__dict__)


foo = Foo('Bavly', 'Moris')
print (foo)

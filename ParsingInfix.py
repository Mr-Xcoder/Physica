# Taken from http://code.activestate.com/recipes/384122/

class Infix:
    def __init__(self, function):
        self.function = function
    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __or__(self, other):
        return self.function(other)
    def __call__(self, value1, value2):
        return self.function(value1, value2)

apply = Infix(lambda function, item: function(item))

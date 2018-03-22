# Inspired by http://code.activestate.com/recipes/384122/

class Infix:
    def __init__(self, func):
        self.func = func
        
    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    
    def __or__(self, other):
        return self.func(other)
    
    def __call__(self, value1, value2):
        return self.func(value1, value2)


Apply = Infix(lambda func, item: func(item))
Map = Infix(lambda func, item: list(map(func, item)))

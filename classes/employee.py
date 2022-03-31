class Employee:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return str(self.name)
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __hash__(self):
        return id(self)

    def __repr__(self):
        return self.__str__()

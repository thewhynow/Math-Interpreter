class NumNode:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"{self.value}"
    
class AddNode:
    def __init__(self, valueA, valueB):
        self.valueA = valueA
        self.valueB = valueB
    
    def __repr__(self):
        return f"({self.valueA} + {self.valueB})"
    
class SubNode:
    def __init__(self, valueA, valueB):
        self.valueA = valueA
        self.valueB = valueB
    
    def __repr__(self):
        return f"({self.valueA} - {self.valueB})"

class MulNode:
    def __init__(self, valueA, valueB):
        self.valueA = valueA
        self.valueB = valueB
    
    def __repr__(self):
        return f"({self.valueA} * {self.valueB})"
    
class DivNode:
    def __init__(self, valueA, valueB):
        self.valueA = valueA
        self.valueB = valueB
    
    def __repr__(self):
        return f"({self.valueA} / {self.valueB})"
    
class PosNode:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"( + {self.value})"

class NegNode:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"( - {self.value})"
from nodes import NumNode
from nodes import AddNode
from nodes import SubNode
from nodes import MulNode
from nodes import DivNode
from nodes import NegNode
from nodes import PosNode
from values import Number

class Interpreter:
    def visit(self, node):
        method = (f"visit_{type(node).__name__}")
        method = getattr(self, method)
        return method(node)

    def visit_NumNode(self, node):
        return Number(node.value)
    
    def visit_AddNode(self, node):
        return Number((self.visit(node.valueA)).value + (self.visit(node.valueB)).value)
    
    def visit_SubNode(self, node):
        return Number((self.visit(node.valueA)).value - (self.visit(node.valueB)).value)
    
    def visit_MulNode(self, node):
        return Number((self.visit(node.valueA)).value * (self.visit(node.valueB)).value)
    
    def visit_DivNode(self, node):
        try:
            return Number((self.visit(node.valueA)).value / (self.visit(node.valueB)).value)
        except:
            raise Exception("You cant type dumbass")
    
    def visit_PosNode(self, node):
        return Number(self.visit(node.value))
    
    def visit_NegNode(self, node):
        return Number( - (self.visit(node.value)).value)

    


from tokens import Token
from nodes import NumNode
from nodes import AddNode
from nodes import SubNode
from nodes import MulNode
from nodes import DivNode
from nodes import PosNode
from nodes import NegNode
global current_index

class Parser:

    def __init__(self, tokens):
        global current_index
        current_index = -1
        self.tokens = tokens
        self.advance()

    def error(self):
        raise Exception("Invalid Syntax")

    def advance(self):
        global current_index
        if not(current_index >= len(self.tokens) - 1):
            current_index += 1
            self.current_token = self.tokens[current_index]

    def parse(self):
        if self.current_token == None:
            return None
        
        result = self.expression()
        return result

    def expression(self):
        result = self.term()

        while self.current_token.type == "ADD" or self.current_token.type == "SUB" and self.current_token != None:

            if self.current_token.type == "ADD":
                self.advance()
                result = AddNode(result, self.term())
                
            
            elif self.current_token.type == "SUB":
                self.advance()
                result = SubNode(result, self.term())
        return result

    def term(self):
        result = self.factor()

        while self.current_token.type == "MUL" or self.current_token.type == "DIV":

            if self.current_token.type == "MUL":
                self.advance()
                result = MulNode(result, self.factor())
            
            elif self.current_token.type == "DIV":
                self.advance()
                result = DivNode(result, self.factor())
        return result
    
    def factor(self):
        
        if self.current_token.type == "NUM":
            factor = NumNode(self.current_token.value)
            self.advance()
            return factor
        
        elif self.current_token.type == "ADD":
            self.advance()
            factor = PosNode(self.factor())
            return factor
        
        elif self.current_token.type == "SUB":
            self.advance()
            factor = NegNode(self.factor())
            return factor
        
        elif self.current_token.type == "LPAREN":
            self.advance()
            result = self.expression()

            if self.current_token.type != "RPAREN":
                self.error()

            self.advance()
            
            return result
        
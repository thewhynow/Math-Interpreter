from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

def main():
    while True:
        text = input("la calculadora > ")
        if text == "stop" or text == "s":
            break
        lexer = Lexer(text)
        lexer.generate_tokens()
        tree = Parser(lexer.tokens)
        tree = tree.parse()
        print(tree)
        interpret = Interpreter()
        interpret = interpret.visit(tree)
        print(interpret)
main()
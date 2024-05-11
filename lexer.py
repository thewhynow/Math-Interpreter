from tokens import Token

global EMPTY, DIGITS

EMPTY = " \n\t"
DIGITS = "0123456789"

class Lexer:
    def __init__(self, text):
        self.text = list(text)

        for i in self.text:
            if i in EMPTY: self.text.remove(i)

        global current_index
        self.tokens = []
        current_index = -1
        self.advance()
    
    def advance(self):
        global current_index
        current_index += 1
        if current_index > len(self.text) - 1:
            self.current_character = None
        else:
            self.current_character = self.text[current_index]

    def generate_tokens(self):
        global current_index
        while self.current_character != None:
            if self.current_character in EMPTY:
                self.advance()
            elif self.current_character in DIGITS or self.current_character == ".":
                self.tokens.append(self.generate_number())
            elif self.current_character == "+":
                self.tokens.append(Token("ADD", None))
                self.advance()
            elif self.current_character == "-":
                self.tokens.append(Token("SUB", None))
                self.advance()
            elif self.current_character == "*":
                self.tokens.append(Token("MUL", None))
                self.advance()
            elif self.current_character == "/":
                self.tokens.append(Token("DIV", None))
                self.advance()
            elif self.current_character == "(":
                self.tokens.append(Token("LPAREN", None))
                if current_index != 0 and (self.text[current_index - 1] in DIGITS or self.text[current_index - 1] == "."):
                    if self.text[current_index - 2] == "-":
                        self.tokens.insert((len(self.tokens) - 1), Token("MUL", None))
                    else:
                        self.tokens.insert((len(self.tokens) - 1), Token("MUL", None))
                elif current_index != 0 and self.text[current_index - 1] == ")":
                    self.tokens.insert((len(self.tokens) - 1), Token("MUL", None))
                self.advance()
            elif self.current_character == ")":
                self.tokens.append(Token("RPAREN", None))
                self.advance()
            else:
                raise Exception("Illegal Character:", self.current_character)
            
    def generate_number(self):
        decimal_point_count = 0
        number_str = self.current_character
        self.advance()

        while self.current_character != None and (self.current_character in DIGITS or self.current_character == "."):
            if self.current_character == ".":
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break
            number_str += self.current_character
            self.advance()

        if number_str.startswith("."):
            number_str = "0" + number_str
        
        if number_str.endswith("."):
            number_str = number_str + "0"
        
        return Token("NUM", float(number_str))
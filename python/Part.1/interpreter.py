# -*- coding: utf-8 -*-
# exercises:
#   1. Modify the code to allow multiple-digit integers in the input, for example “12+3”
#   2. Add a method that skips whitespace characters so that your calculator can handle inputs with whitespace characters like ” 12 + 3”
#   3. Modify the code and instead of ‘+’ handle ‘-‘ to evaluate subtractions like “7-5”

import token

class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None

    def express(self):
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat(token.TOKEN_INTEGER)

        op = self.current_token
        self.eat(token.TOKEN_MINUS)

        right = self.current_token
        self.eat(token.TOKEN_INTEGER)

        result = left.value - right.value
        return result

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def get_next_token(self):
        text = self.text
        tk = None

        if self.pos > len(text) - 1:
            return token.Token(token.TOKEN_EOF, None)

        current_char = text[self.pos]

        while current_char == ' ':
            self.pos += 1
            if self.pos >= len(text):
                break;
            current_char = text[self.pos]

        if self.pos >= len(text):
            return token.Token(token.TOKEN_EOF, None)

        if current_char.isdigit():
            num = int(current_char)
            while self.pos < len(text) - 1 and text[self.pos + 1].isdigit():
                self.pos += 1
                num = num * 10 + int(text[self.pos])
            tk = token.Token(token.TOKEN_INTEGER, int(num))
        elif current_char == '+':
            tk = token.Token(token.TOKEN_PLUS, '+')
        elif current_char == '-':
            tk = token.Token(token.TOKEN_MINUS, '-')
        
        if tk == None:
            self.error()

        self.pos += 1
        return tk

    def error(self):
        raise Exception("Parsing Error")
        
    
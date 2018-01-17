# -*- coding: utf-8 -*-

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
        self.eat(token.TOKEN_PLUS)

        right = self.current_token
        self.eat(token.TOKEN_INTEGER)

        result = left.value + right.value
        return result

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def get_next_token(self):
        text = self.text

        if self.pos > len(text) - 1:
            return token.Token(token.TOKEN_EOF, None)

        current_char = text[self.pos]
        tk = None

        if current_char.isdigit():
            tk = token.Token(token.TOKEN_INTEGER, int(current_char))

        if current_char == '+':
            tk = token.Token(token.TOKEN_PLUS, '+')
        
        if tk == None:
            self.error()

        self.pos += 1
        return tk

    def error(self):
        raise Exception("Parsing Error")
        
    
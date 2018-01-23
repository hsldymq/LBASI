# -*- coding: utf-8 -*-

TOKEN_INTEGER = 'INTEGER'
TOKEN_PLUS = 'PLUS'
TOKEN_MINUS = 'MINUS'
TOKEN_EOF = 'EOF'

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return "Token({type}, {value})".format(type = self.type, value = repr(self.value))

    def __repr(self):
        return self.__str__()

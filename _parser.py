from _lexer import *
from _ast import *

class Parser(object):
    def __init__(self,lexer):
        self.lexer = lexer
        self.current_token  = self.lexer.get_next_token()
    
    def eat(self,token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(token_type,self.lexer.column,self.lexer.line)
    
    def error(self,expected, column, line):
        return Exception('Expected: {} ')
    def parse(self):
        print("Parsing..")
        return AST()

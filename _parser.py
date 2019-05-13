from _lexer import *
from _ast import *

class Parser(object):
    def __init__(self,lexer):
        self.lexer = lexer
        self.current_token  = self.lexer.get_next_token()
    
    def parse(self):
        print("Parsing..")
        return AST()

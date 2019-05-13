from _lexer import *
from _ast import *
from tokens import *
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
        raise Exception('Syntax error at col: {}, line: {} !\nExpected: {}'.format(column,line,expected))
    
    '''
    BLOCK: BLOCK
    | LPAREN EXPR RPAREN
    | LPAREN FUNC ARGS RPAREN
    '''
    def block(self):
        self.eat(LPARAN)

        if self.current_token.type == LPARAN:
            self.block()
        # elif self.current_token == ID:
          # self._id()
          
        self.eat(RPARAN)
        return AST()
    
    def parse(self):
        node  = self.block()
        return node

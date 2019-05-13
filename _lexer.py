from tokens import *
class Lexer:
    def __init__(self,code,length):
        self.code = code
        self.line = 0
        self.column = 0
        self.length  = length
        self.pos = 0
        self.current_char  = self.code[self.line][self.column]
        self.current_token = None
    
    def skip_space(self):
        while self.current_char == ' ' or self.current_char == '\n' and self.current_char is not None:
            self.advance()
    
    def get_id(self):
        _id = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            _id  += self.current_char
            self.advance()
        return _id
    
    def peek(self):
        peek_column = self.column + 1
        peek_pos = self.pos + 1
        peek_line = self.line

        if peek_pos > self.length - 1 :
            return None
        
        elif peek_column > len(self.code[peek_line]) - 1 :
            peek_line += 1
            peek_column = 0
        
        if peek_line > len(self.code) - 1:
            return None
        return self.code[peek_line][peek_column]
        
    def advance(self):
        self.column += 1
        self.pos += 1

        if self.pos > self.length - 1 :
            self.current_char = None
            return
        
        elif self.column > len(self.code[self.line]) - 1 :
            self.line += 1
            self.column = 0
        if self.line > len(self.code) - 1:
            self.current_char = None
            return
        
        

        self.current_char = self.code[self.line][self.column]
    
    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_space()
                continue

            if self.current_char == '(':
                self.advance()
                return Token(LPARAN,'(')
        
            if self.current_char == ')':
                self.advance()
                return Token(RPARAN,')')

            if self.current_char.isalpha() or self.current_char == '_':
                return self.get_id()
            
            return Token(INVALID_CHARACTER,self.current_char)
            
        return Token(EOF,'end')
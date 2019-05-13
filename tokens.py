class Token:
    def __init__(self, type, value):
        self.type = type
        self.value  = value
    
    def __str__(self):
        return 'Token({},\'{}\')'.format(self.type,self.value)

# Tokens
LPARAN = 'LPARAN'
RPARAN = 'RPARAN'

QUOTES='QUOTES'
COMMA='COMMA'
INVALID_CHARACTER='INVALID_CHARACTER'
EOF='EOF'
SPACE='SPACE'

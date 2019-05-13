from _lexer import Lexer
from _parser import *

import sys
import os


def main(argc,argv):
    if argc != 2:
        print('brscript <filename>.br')
        return 1
    filename = argv[1]
    lexer = Lexer(open(filename).readlines(),os.path.getsize(filename))
    par = Parser(lexer)
    tree = par.parse()

main(len(sys.argv),sys.argv)

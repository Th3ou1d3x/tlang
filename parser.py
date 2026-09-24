from __future__ import annotations
import lexer
import sys
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from _typeshed import SupportsWrite
def terror(name, value, debugflag:bool=False,debugFile: SupportsWrite[str]|None=sys.stderr, exitcode:int=1):
    print(f"{name}: {value}", file=sys.stderr if not debugflag else debugFile)
    sys.exit(exitcode)
class ast:
    def __init__(self, ast: dict):
        self.ast = ast
class parser:
    def __init__(self, tokens: lexer.Tokens, debugFile: SupportsWrite[str]|None=None, debugflag: bool = False):
        self.tokens = tokens.tokens
        self.debug = debugFile
        self.debugflag = debugflag
    def parse(self):
        AST={}
        for token in self.tokens:
            continue
        return ast(AST)
    def parse_token(self):
        pass
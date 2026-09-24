from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from _typeshed import SupportsWrite
import sys
def terror(name, value, debugflag:bool=False,debugFile: SupportsWrite[str]|None=sys.stderr, exitcode:int=1):
    print(f"{name}: {value}", file=sys.stderr if not debugflag else debugFile)
    sys.exit(exitcode)
class Tokens:
    def __init__(self, tokens: list):
        self.tokens = tokens
class Lex:
    def __init__(self, filepath, debugFile: SupportsWrite[str]|None=None, debugflag: bool = False):
        self.file = filepath
        self.keywords = ["let", "const", "$include", "$import", "ret", "asm", "if", "$entry", "proc"]
        self.tokens = []
        self.debug = debugFile
        self.debugflag = debugflag
    def tokenize(self):
        with open(self.file) as f:
            dat = f.read()
        word = ""
        state = 0
        c = 0
        state2 = 0
        for ln in dat.splitlines():
            state = 0 if state != 2 else state
            for word in ln.split():
                c += 1
                if word == "#":
                    if state == 0 or state == 1:
                        state2 = state
                        state = 2
                        self.tokens.append(("COMMENT", 0))
                        continue
                    else:
                        state = state2
                        state2 = 0
                        self.tokens.append(("COMMENT", 1))
                        continue
                if state == 2:
                    continue
                if word in self.keywords:
                    self.tokens.append(("KEYWORD", word))
                    state = 1
                    continue
                elif state == 1:
                    self.tokens.append(("ARG", word))
        return Tokens(self.tokens)
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from _typeshed import SupportsWrite
import sys
import parser
def terror(name, value, debugflag:bool=False,debugFile: SupportsWrite[str]|None=sys.stderr, exitcode:int=1):
    print(f"{name}: {value}", file=sys.stderr if not debugflag else debugFile)
    sys.exit(exitcode)
class emitter:
    def __init__(self, ast: parser.ast, target: str, output: str, debugFile: SupportsWrite[str]|None=None, debugflag: bool = False):
        self.ast = ast.ast
        self.debug = debugFile
        self.debugflag = debugflag
        self.target = target.lower().strip()
        self.output = output
    def emit(self):
        if not self.target in ["x86_64"]: # , "x86_32", "arm64", "arm32"
            terror("TTargetError", "Target must be one of: [\"x86_64\",\"x86_32\",\"arm64\",\"arm32\"]. note: these are targets we WILL add, only x86_64 is added rn", self.debugflag, self.debug)

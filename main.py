import sys
import random
keychars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
def parse_args(args: list):
    reparse = {
        "-i": "--input",
        "-o": "--output"
    }
    narg = []
    skip = False
    key = ""
    flg = []
    for i in range(10):
        key += random.choice(keychars)
    i = -1
    key = "//blocker"+ key +"//"
    for arg in args:
        i = i + 1
        if skip:
            skip = False
            continue
        if arg.startswith("-"):
            if arg in reparse.keys():
                arg = reparse[arg]
            flg.append(arg)
            narg.append(arg + key + args[i+1])
            skip = True
            continue
        narg.append(arg)
    c = 0
    c2 = ["--input", "--output"]
    narg2 = {}
    for arg in narg:
        if not key in arg:
            if c > 1:
                if not c2[c] in flg:
                    narg2[c2[c]] = arg
                    continue
            c += 1
        narg2[arg.split(key)[0]] = arg.split(key)[1]
    return narg2
args = parse_args(sys.argv[1:])
debug = False
file = None
if "--debug" in args:
    debug = True
    file = args["--debug"]
import lexer
lex = lexer.Lex(args["--input"], file, debug)
tokens = lex.tokenize()
print(tokens.tokens)
import parser
Parser = parser.parser(tokens, file, debug)
ast = Parser.parse()
import emitter
Emitter = emitter.emitter(ast, args["--output"], file, debug)

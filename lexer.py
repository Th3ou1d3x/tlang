class Lex:
    def __init__(self, filepath):
        self.file = filepath
        self.keywords = ["let", "const", "$include", "$import", "ret", "asm", "if"]
        self.tokens = []
    def tokenize(self):
        with open(self.file) as f:
            dat = f.read()
        word = ""
        state = 0
        c = 0
        for ln in dat.splitlines():
            state = 0
            for word in ln.split():
                c += 1
                if word in self.keywords:
                    self.tokens.append(("KEYWORD", word))
                    state = 1
                    continue
                elif state == 1:
                    self.tokens.append(("ARG", word))

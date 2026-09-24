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
        for char in dat:
            if char == "\n":
                word = ""
                continue
            word = f"{word}{char}"
            if word in self.keywords:
                break
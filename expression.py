class Expression:
    def __init__(self, line):
        self.line = line

    def evaluate(self):
        try:
            result = str(eval(self.line))
        except:
            result = "ERROR!"
        return result
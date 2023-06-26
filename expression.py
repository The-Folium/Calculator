from math import *

class Expression:
    def __init__(self, line):
        self.line = line

    def evaluate(self):
        while function_pos:=self.line.find("log(") != -1:
            line = self.line
            self.line = line[:function_pos+2]+'10'+line[function_pos+2:]

        try:
            result = str(round(eval(self.line), 12))
        except ZeroDivisionError:
            result = "Division by Zero Error"
        except ValueError:
            result = "Math Error"
        except:
            result = "Syntax Error"

        return result

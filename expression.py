from math import *

class Expression:
    def __init__(self, line):
        self.line = line

    def evaluate(self):
        # for function in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan',
        #                  'sqrt', 'log', 'exp', 'pi']:
        #
        #     if function_pos:=self.line.find(function) != -1:
        #
        #         line = self.line
        #         self.line = line[:function_pos-1]+'math.'+line[function_pos-1:]
        while function_pos:=self.line.find("log(") != -1:
            line = self.line
            self.line = line[:function_pos+2]+'10'+line[function_pos+2:]
        # print(self.line)
        try:
            result = str(round(eval(self.line), 12))
        except ZeroDivisionError:
            result = "Division by Zero Error"
        except ValueError:
            result = "Math Error"
        except:
            result = "Syntax Error"

        return result

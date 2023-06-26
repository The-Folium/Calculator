import math

class Expression:
    def __init__(self, line):
        self.line = line

    def evaluate(self):
        print(self.line)
        for function in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan',
                         'sqrt', 'log', 'exp', 'pi']:
            if function_pos:=self.line.find(function) != -1:
                line = self.line
                self.line = line[:function_pos-1]+'math.'+line[function_pos-1:]
        print(self.line)
        try:
            result = str(eval(self.line))
        except ZeroDivisionError:
            result = "Division by Zero Error"
        except ValueError:
            result = "Math Error"
        except:
            result = "Syntax Error"

        return result

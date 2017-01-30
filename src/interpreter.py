import hParser as parser
import sys
from math import floor
from itertools import cycle


class EndException(Exception):
    pass


class Interpreter:
    def __init__(self, code):
        self.code = code
        self.stacks = [[], [], [], []]
        self.current_stack = 3
        self.commands = []
        self.out = None

    def eval(self):
        try:
            for tok in cycle(parser.parse(self.code)):
                self.eval_token(tok)
        except EndException:
            pass

    def eval_token(self, tok):
        if tok[0] == '형':
            self.push(self.current_stack, tok[1] * tok[2])
        elif tok[0] == '항':
            res = 0
            for _ in range(tok[1]):
                val = self.pop(self.current_stack)
                if val is None:
                    res = None
                elif res is not None:
                    res += val
            self.push(tok[2], res)
        elif tok[0] == '핫':
            res = 1
            for _ in range(tok[1]):
                val = self.pop(self.current_stack)
                if val is None:
                    res = None
                elif res is not None:
                    res *= val
            self.push(tok[2], res)
        elif tok[0] == '흣':
            temp = []
            for _ in range(tok[1]):
                val = self.pop(self.current_stack)
                if val is not None:
                    temp.insert(0, -1 * val)
                else:
                    temp.insert(0, val)
            if None in temp:
                res = None
            else:
                res = sum(temp)
            for _ in range(tok[1]):
                self.push(self.current_stack, temp.pop())
            self.push(tok[2], res)
        elif tok[0] == '흡':
            temp = []
            res = 1
            for _ in range(tok[1]):
                val = self.pop(self.current_stack)
                if val is not None:
                    if val == 0:
                        val = None
                    else:
                        val = 1 / val
                        if res is not None:
                            res *= val
                else:
                    res = None
                temp.insert(0, val)
            for _ in range(tok[1]):
                self.push(self.current_stack, temp.pop())
            self.push(tok[2], res)
        elif tok[0] == '흑':
            val = self.pop(self.current_stack)
            self.push(self.current_stack, val)
            for _ in range(tok[1]):
                self.push(tok[2], val)
            self.current_stack = tok[2]

    def push(self, stack, value):
        while len(self.stacks) <= stack:
            self.stacks.append([])
        if stack == 1 and self.out is not None:
            if value is None:
                self.out.write('너무 커엇...')
                self.out.flush()
                return
            elif type(value) is float:
                value = floor(value)
            if value > 0:
                self.out.write(chr(value))
            if value < 0:
                self.out.write(str(-1 * value))
            self.out.flush()
        else:
            self.stacks[stack].append(value)

    def pop(self, stack):
        if stack == 1:
            raise EndException
        if stack == 2:
            raise IndexError()
        while len(self.stacks) <= stack:
            self.stacks.append([])
        if len(self.stacks[stack]) == 0:
            return None
        return self.stacks[stack].pop()

if __name__ == '__main__':
    interpreter = Interpreter('혀어어어어어어어엉........ 핫. 혀엉..... 흑... 하앗... 흐윽... 형.  하앙.혀엉.... 하앙... 흐윽... 항. 항. 형... 하앙. '
                              '흐으윽... 형... 흡... 혀엉..하아아앗. 혀엉.. 흡... 흐읍... 형.. 하앗. 하아앙... 형... 하앙... 흐윽...혀어어엉.. 하앙. '
                              '항. 형... 하앙. 혀엉.... 하앙. 흑... 항. 형... 흡  하앗.혀엉..... 흑. 흣')
    interpreter.out = sys.stdout
    interpreter.eval()

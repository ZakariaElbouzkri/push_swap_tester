# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'

OK = GREEN + BOLD + "OK" + RESET
KO = RED + BOLD + "KO" + RESET

ops = ["sa", "sb", "ss", "ra", "rb", "rr", "rra", "rrb", "rrr", "pa", "pb"]

# set timeout with seconds
TIMEOUT = 3 # seconds

class Checker:
    def __init__(self, numbers=[], instractions=[]) -> None:
        self.numbers : list = numbers
        self.instractions : list = instractions
        self.status = None

    def setNumbers(self, numbers):
        self.numbers = numbers

    def setInstractions(self, instractions):
        self.instractions = instractions

    def check(self) -> None:
        if len(self.instractions) == 0 and len(self.numbers) == 0:
            return
        stackA = self.numbers
        stackB = []
        self.status = KO
        for op in self.instractions:
            if op not in ops:
                break
            if op == "sa" or op == "ss" and len(stackA) > 1:
                stackA[0], stackA[1] = stackA[1], stackA[0]
            if op == "sb" or op == "ss" and len(stackB) > 1:
                stackB[0], stackB[1] = stackB[1], stackB[0]
            if op == "ra" or op == "rr" and len(stackA) > 1:
                stackA.append(stackA.pop(0))
            if op == "rb" or op == "rr" and len(stackB) > 1:
                stackB.append(stackB.pop(0))
            if op == "rra" or op == "rrr" and len(stackA) > 1:
                stackA.insert(0, stackA.pop(-1))
            if op == "rrb" or op == "rrr" and len(stackB) > 1:
                stackB.insert(0, stackB.pop(-1))
            if op == "pa" and len(stackB) > 0:
                stackA.insert(0, stackB.pop(0))
            if op == "pb" and len(stackA) > 0:
                stackB.insert(0, stackA.pop(0))
        if len(stackB) == 0 and all(stackA[i] <= stackA[i + 1] for i in range(len(stackA) - 1)):
            self.status = OK


import subprocess , sys
from checker import *
import random


def geneate_numbers(start, end, size=100):
    numbers = set()
    if end <= start:
        return [-1]
    if end - start < size:
        size = end - start - 1
    while len(numbers) != size:
        numbers.add(random.randint(start, end))    
    numbers = list(numbers)
    random.shuffle(numbers)
    return numbers

class Tester:
    def __init__(self, ps_dir: str, start, end, size) -> None:
        self.ps = ps_dir
        self.checker = Checker()
        self.results = []
        self.start = start if start is not None else -100000
        self.end = end if end is not None else 100000
        self.size = size if size is not None else 100

    def getInstractionsColor(self, stackSize, n):
        color = BLUE
        if stackSize <= 2 and n > 1 or stackSize == 3 and n > 2 or stackSize == 5 and n > 12:
            color = RED
        elif stackSize <= 100 or stackSize <= 500:
            if stackSize <= 100 and n < 700 or stackSize <= 500 and n < 5500:
                color = BLUE
            elif stackSize <= 100 and n < 900 or stackSize <= 500 and n < 7000:
                color = CYAN
            elif stackSize <= 100 and n < 1100 or stackSize <= 500 and n < 8500:
                color = GREEN
            elif stackSize <= 100 and n < 1300 or stackSize <= 500 and n < 10000:
                color = YELLOW
            elif stackSize <= 100 and n < 1500 or stackSize <= 500 and n < 11500:
                color = MAGENTA
            else:
                color = RED
        return color

    def Test(self):
        numbers = geneate_numbers(start=self.start, end=self.end, size=self.size)
        args = [self.ps] + [str(num) for num in numbers]
        self.results = []
        try:
            process = subprocess.run(args, capture_output=True, text=True, timeout=TIMEOUT)
            if process.returncode != 0:
                raise subprocess.CalledProcessError(returncode=process.returncode, cmd=args[0])
            instractions = process.stdout.split()
            self.checker.instractions = instractions
            self.checker.numbers = numbers.copy()
            self.checker.check()
            self.results.append(f"Sorted: {self.checker.status}")
            numberInstractions = f"{BOLD + self.getInstractionsColor(self.size, len(instractions))}{len(instractions)}{RESET}"
            self.results.append(f"Number of instraction : {numberInstractions}")
        except subprocess.TimeoutExpired:
            self.results.append(f"Sorted: {KO}")
            self.results.append(f"{YELLOW + BOLD}Time limit exceeded {RESET}")
        except subprocess.CalledProcessError:
            self.results.append(f"Sorted: {KO}")
            self.results.append(f"{RED + BOLD}Runtime error (crash) {RESET}")
        except Exception:
            print("tester: Error Occured during test", file=sys.stderr)
            sys.exit(1)
        numbers = " ".join([str(num) for num in numbers])
        self.results.append(f"Tester Stack : {numbers}")


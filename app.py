#!/usr/local/bin/python3

import tkinter
import random
import sys
import subprocess
import re


red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[94m'
reset = '\033[0m'

import os

pt = '\-?[0-9]+$'

def usage():
    sys.stderr.write("usage :")
    sys.stderr.write("\t 1: -n [your args]")
    sys.stderr.write("\t 2: let program generate numbers: start, end, size\n")
    sys.exit(1)

def generate_nums(start, end, size):
    if re.match(pt, start) and re.match(pt, end) and re.match(pt, size):
        start, end, size = int(start), int(end), int(size)
        if size > 2 and (end - start) > size:
            nums = set()
            while len(nums) < size:
                nums.add(random.randint(start, end))
            return nums
    return None


relative_path = f"{os.getcwd()}"

# push_swap program
push_swap = f"{relative_path}/push_swap"

# checker program
checker = f"{relative_path}/checker"


# check if the program checker and push_swap are in the path
if not os.access(push_swap, os.X_OK):
    sys.stderr.write("push_swap not found")
if not os.access(checker, os.X_OK):
    sys.stderr.write("checker not found")

# argv
args = sys.argv[1:]

if len(args) < 3:
    usage()

nums = ''
if args[0] == '-n':
    nums = args[1:]

else:
    nums = generate_nums(args[0], args[1], args[2])
    if not nums:
        sys.stderr.write("Invalid args")
        sys.exit(1)
    nums = list(map(str, nums))
    # nums = " ".join(str(nums))


ops = subprocess.run([push_swap] + nums, capture_output=True, text=True)
if ops.returncode != 0:
    sys.stderr.write(f"push_swap output: {ops.stderr}")
    sys.exit(1)

with open('op.log', 'w') as f:
    f.write(ops.stdout)

ops = ops.stdout.split('\n')

status = subprocess.run([checker] + nums,capture_output=True, text=True, stdin=open('op.log'))
if status.returncode != 0:
    sys.stderr.write(f"checker: {status.stderr}")
    sys.exit(1)

if status.stdout == 'OK\n':
    print(f"Sorted: {green}OK{reset}")
    print(f"Number of Instractions:{blue}{len(ops)-1}{reset}")
    print(f"numbers: {yellow}")
    print(*nums, sep=' ')
else:
	print(red + 'KO' + reset)


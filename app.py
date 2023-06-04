#!/usr/local/bin/python3


import random
import sys
import subprocess
import re
import tempfile
import time


red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[94m'
reset = '\033[0m'

import os

# pattern of of digit
pt = '\-?[0-9]+$'

"""
        function that displays usage of the
        program if argument not gived correctlys and exit process
        it dosn't takes any argument 
"""
def usage():
    sys.stderr.write("usage :")
    sys.stderr.write("\t 1: -n [your args]")
    sys.stderr.write("\t 2: let program generate numbers: start, end, size\n")
    sys.exit(1)

"""
    function that generate random value
    params:
        start: start of range that you will test
        end: end of range
        size: len of numbers list
    returns:
        reandom numbers that generated
        None if param not gived correctly
"""
def generate_nums(start, end, size):
    nums = set()
    while len(nums) < size:
        nums.add(random.randint(start, end))
    nums = list(nums)
    random.shuffle(nums)
    return  nums



def parse_input(argv):
    start, end, size = argv[0], argv[1], argv[2]
    test_case = 1
    if (len(argv) >= 4):
        if re.match(pt, argv[3]):
            test_case = abs(int(args[3]))
            test_case -= (test_case > 100) * (test_case - 100)

    if re.match(pt, start) and re.match(pt, end) and re.match(pt, size):
        start, end, size = int(start), int(end), int(size)
        if size >= 2 and (end - start) >= size:
            return [start, end, size, test_case]
    return None

def display_results(n, nums, size):
    color = green
    if size == 2 or (size == 3 and n < 2) or (size < 5 and n < 12) or (size <= 100 and n <= 700) or (size <= 500 and n <= 5400):
        color = blue
    print(f"Sorted : {color}OK{reset}")
    print(f"Number of instractions : {color}{n}{reset}")
    print(f"Tested number : {yellow}")
    print(*nums, sep=' ')
    print(f"{reset}", end='')

def display_fail(tested_nums, **args):
    if args.get('time_out'):
        print(f"{red}Time out")
    elif args.get('err'):
        if (out := args.get('stdout')):
            print(f"Stdout stream :{red}{out}")
    else:
        print(f"sorted: {red}KO{reset}")
        print(f"Stdout stream :")
        if (out := args.get('res')):
            print(f"Sorted: {red} KO{reset}")
        if (out := args.get('stdout')):
            print('push_swap :')
            print(out)
        if (out := args.get('checker')):
            print('push_swap :')
            print(out)
    print(f"{reset}Tested number :")
    print(*tested_nums, sep=' ')
        
        


def test(push_swap, checker, start=0, end=0, size=0, test_case_number=1, nums=None):
    # generate random file
    for i in range(test_case_number):
        tmp = tempfile.TemporaryFile(mode='w')
        if nums is None:
            nums = generate_nums(start, end, size)
            nums = list(map(str, nums))
        # exec push_swap
        print(f"Test {i+1} :")
        try:
            ops = subprocess.run([push_swap] + nums, capture_output=True, text=True, timeout=15)
        except subprocess.TimeoutExpired:
            display_fail(nums, err=1, stdout=ops.stdout)
        if ops.returncode != 0:
            display_fail(nums, stdout=ops.stderr)
        tmp.write(ops.stdout)
        tmp.seek(0)
        n_ops = len(ops.stdout.split('\n')) - 1
        try:
            status = subprocess.run([checker] + nums, capture_output=True, text=True, stdin=tmp, timeout=15)
        except subprocess.TimeoutExpired:
            display_fail(nums, time_out=1)

        if status.returncode != 0:
            display_fail(nums, push_swap=ops.stdout, checker=status.stderr)

        if status.stdout == 'OK\n':
            display_results(n_ops, nums, size)
        else:
            display_fail(nums, res="OK")
        print(f"{reset}")
        nums = None
        time.sleep(0.6)
        tmp.close()

def get_path(file_name):
    curr = f"{os.getcwd()}"
    path = f"{curr}/{file_name}"
    if not os.access(file_name, os.X_OK):
        sys.stderr.write(f"{file_name}: not found\n")
        sys.exit(1)
    return path

if __name__=='__main__':
    push_swap = get_path("push_swap")
    checker = get_path("checker")
    args = sys.argv[1:]
    if (args[0] == '-n'):
        test(push_swap, checker, nums=args[1:])
    inp = parse_input(args)
    if inp is None or len(args) < 3:
        usage()
    start, end, size, test_cases = inp
    test(push_swap, checker, start, end, size, test_cases)

# # argv
# args = sys.argv[1:]

# if len(args) < 3:
#     usage()

# if args[0] == '-n':
#     nums = args[1:]
#     test(push_swap, checker,)
# else:
#     res = parse_input(args)
#     if res is not None:
#         start, end, size, test_n = res
#         test(push_swap, checker, start, end, size, test_n)
#     else:
#         usage()


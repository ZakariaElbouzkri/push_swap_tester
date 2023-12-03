
from tester import Tester
import os, sys, time


def main():
    ps_dir = os.path.join(os.getcwd(), "push_swap") # join current_dir with push_swap executable
    if not os.access(ps_dir, os.X_OK): # check if the executable exist and can be executed
        print("push_swap not found or not executable")
        sys.exit(1)
    args = sys.argv[1:]
    # extract N number of test and size Stack size [start, end] ranges of numbers from argv the default is None
    N, size, start, end = [int(args[i]) if len(args) > i and args[i].isdigit() else None for i in range(4)]
    N = N if N is not None else 2
    tester = Tester(ps_dir, start, end, size) # create Tester
    for _ in range(N):
        tester.Test() 
        for info in tester.results:
            print(info)
        print()
        time.sleep(0.6)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Done")






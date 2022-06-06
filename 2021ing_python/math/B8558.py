import sys
from math import factorial

IN = sys.stdin.readline

if __name__ == "__main__":
    n = int(IN())
    print(str(factorial(n))[-1])
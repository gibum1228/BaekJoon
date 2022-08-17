import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    a = int(IN())
    x = int(IN())
    b = int(IN())
    y = int(IN())
    T = int(IN())
    A = a + max(T - 30, 0) * x * 21
    B = b + max(T - 45, 0) * y * 21
    print(A, B)
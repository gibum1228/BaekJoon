import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    Ca, Ba, Pa = map(int, input().split())
    Cr, Br, Pr = map(int, input().split())
    ans = max(0, Cr - Ca) + max(0, Br - Ba) + max(0, Pr - Pa)
    print(ans)
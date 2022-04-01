import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    M, S = map(int, IN().split(":"))
    count = 0
    
    T = M * 60 + S
    if T < 30:
        print(T // 10 + 1)
    else:
        count += 1
        T -= 30
        count += T // 600
        T %= 600
        count += T // 60
        T %= 60
        count += T // 30
        T %= 30
        count += T // 10
        
        print(count)
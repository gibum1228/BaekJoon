import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    a = IN().rstrip()
    b = IN().rstrip()
    c = IN().rstrip()
    arr = list(map(int, list('9780921418' + a + b + c)))
    results = 0

    for i in range(len(arr)):
        if i % 2 == 0:
            results += arr[i]
        else:
            results += arr[i] * 3

    print(f"The 1-3-sum is {results}")
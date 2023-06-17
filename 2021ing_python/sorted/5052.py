import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(IN())):
        trigger = True
        arr = [IN().rstrip() for _ in range(int(IN()))]
        arr.sort()

        for i in range(len(arr)-1):
            if arr[i] == arr[i+1][:len(arr[i])]:
                trigger = False
                break

        print("YES" if trigger else "NO")
n = int(input())

numbers = list(map(int, input().split()))

for i in sorted(set(numbers)):
    print(i, end = " ")
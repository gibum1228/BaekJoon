t = int(input())

for i in range(t):
    lists = list(map(int, input().split()))
    lists.sort()
    print(lists[-3])
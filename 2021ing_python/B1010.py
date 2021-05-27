import math

T = int(input())

for i in range(T):
    r, n = map(int, input().split())
    print(math.factorial(n) // (math.factorial(r) * math.factorial(n-r)))
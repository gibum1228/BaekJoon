import math

A, B = map(int, input().split())
m = int(input())
inputs = list(map(int, input().split()))
results = []

num_a = 0
for i in range(m-1, -1, -1):
    num_a += (inputs[m-1-i]*math.pow(A, i))

while True:
    results.append(int(num_a % B))
    num_a //= B
    if num_a == 0:
        break

print(" ".join(list(map(str, results[::-1]))))
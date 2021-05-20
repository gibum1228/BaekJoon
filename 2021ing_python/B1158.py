n, k = map(int, input().split())
people = [i for i in range(1, n+1)]
results = []
index = 0

while len(people) > 0:
    index = (index + (k-1)) % len(people)
    results.append(str(people.pop(index)))

print("<%s>" %", ".join(results))
results = [[] for i in range(5)]
result = [[] for i in range(15)]

for i in range(5):
    results[i] = list(input())

for i in range(5):
    for j in range(len(results[i])):
        result[j].append(results[i][j])

print("".join(sum(result, [])))
import sys

N = int(sys.stdin.readline())
results = list()

for i in range(N):
    name, k, e, m = sys.stdin.readline().split()
    k, e, m = int(k), int(e), int(m)

    results.append({
        'name': name, 'k': k, 'e': e, 'm': m
    })

results = sorted(results, key = lambda x : (-x['k'], x['e'], -x['m'], x['name']))

for i in results:
    print(i['name'])
sequence = []
i = 0
j = 1

while len(sequence) != 1000:
    if i == j:
        i = 0
        j += 1

    sequence.append(j)

    i += 1

A, B = map(int, input().split())

print(sum(sequence[A-1:B]))
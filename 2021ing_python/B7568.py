N = int(input()) # 사람 수

people = [ # 사람 정보 리스트
    { 'weight': 0, 'height': 0, 'rank': 1} for _ in range(N)
]

# input
for i in range(N):
    w, h = map(int, input().split())

    people[i]['weight'] = w
    people[i]['height'] = h

# compare
for i in range(N):
    for j in range(N):
        if people[i]['weight'] < people[j]['weight'] and people[i]['height'] < people[j]['height']:
            people[i]['rank'] += 1

# print
for _ in range(N):
    print(people[_]['rank'], end=" ")

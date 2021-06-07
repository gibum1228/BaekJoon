bingo = []
check = [[False for _ in range(5)] for _ in range(5)]
count_bingo = 0
count = 0

for i in range(5):
    bingo.append(list(map(int, input().split())))

for _ in range(5):
    for n in list(map(int, input().split())):
        count += 1
        for i in range(5):
            if bingo[i].count(n) == 1:
                j = bingo[i].index(n)
                check[i][j] = True

                if check[i].count(True) == 5:
                    count_bingo += 1

                stack = 0
                for k in range(5):
                    if check[k][j] == True:
                        stack += 1
                if stack == 5:
                    count_bingo += 1

                if i == j:
                    a = 0
                    for l in range(5):
                        if check[l][l]:
                            a += 1
                    if a == 5:
                        count_bingo += 1

                if i + j == 4:
                    b = 0
                    for l in range(5):
                        if check[l][4 - l]:
                            b += 1
                    if b == 5:
                        count_bingo += 1

        if count_bingo >= 3:
            print(count)
            exit()

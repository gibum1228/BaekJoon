import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    db = {chr(k): [] for k in range(65, 65+26)}
    arr = IN().rstrip()

    for i, s in enumerate(arr):
        db[s].append(i)

    result = []
    for i in range(52):
        for j in range(i+1, 52):
            if db[arr[i]][0] < db[arr[j]][0] < db[arr[i]][1] < db[arr[j]][1] or db[arr[i]][0] > db[arr[j]][0] > db[arr[i]][1] > db[arr[j]][1]:
                if arr[i] != arr[j] and set([arr[i], arr[j]]) not in result:
                    result.append(set([arr[i], arr[j]])) # 경로가 만나고, 이미 찾은 답이 아니라면 추가

    print(len(result))
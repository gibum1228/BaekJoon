import sys

len_log = int(sys.stdin.readline()) # 입력 속도 향상
dic_log = {}

for i in range(len_log):
    name, operator = sys.stdin.readline().split()

    if operator == "enter":
        dic_log[name] = 1
    else:
        del dic_log[name]

print("\n".join(sorted(dic_log.keys(), reverse=True)))
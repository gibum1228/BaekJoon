import re


if __name__ == "__main__":
    problem = input()

    # 정규식
    oper_arr = re.compile('[+-]+').findall(problem)
    num_arr = re.compile('[0-9]+').findall(problem)

    # plus
    while True:
        try:
            focus = oper_arr.index("+")
        except:
            break

        oper_arr.pop(focus)

        num_arr[focus] = int(num_arr[focus]) + int(num_arr[focus+1])
        num_arr.pop(focus+1)

    # minus
    while True:
        try:
            focus = oper_arr.index("-")
        except:
            break

        oper_arr.pop(focus)

        num_arr[focus] = int(num_arr[focus]) - int(num_arr[focus + 1])
        num_arr.pop(focus + 1)

    print(num_arr[0])
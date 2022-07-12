import math
import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    result = ""
    l1_role, l2_role, l3_role = math.ceil(35 * 0.3), math.ceil(25 * 0.3), math.ceil(40 * 0.3)

    for i in range(N):
        id, l1, l2, l3 = map(int, IN().split())
        sum_num = l1 + l2 + l3

        if sum_num >= 55 and l1 >= l1_role and l2 >= l2_role and l3 >= l3_role:
            result += f"{id} {sum_num} PASS\n"
        else:
            result += f"{id} {sum_num} FAIL\n"

    print(result)
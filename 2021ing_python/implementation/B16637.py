import sys
from collections import deque
import copy

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())

    if N == 1:
        print(int(IN()))
    else:
        ### 숫자와 연산자 분리
        original_numbers = dict()
        original_operators = dict()
        for x in list(IN().rstrip()):
            if x.isdigit():
                original_numbers[len(original_numbers)] = int(x)
            else:
                original_operators[len(original_operators)] = x
        # print("원본")
        # print(original_numbers)
        # print(original_operators)
        ### 연산자 조합 찾기
        combinations = []
        que = deque([[True], [False]]) # 첫 번째 연산자가 ()냐 아니냐로 조합 시작
        while que:
            combi = que.popleft()

            if len(combi) == len(original_operators): # operators와 길이가 똑같으면 조합 찾기 스탑
                combinations.append(combi)
            else:
                if combi[-1]: # 바로 전 연산자에 ()가 있다면 -> ()가 없는 경우만 존재
                    que.append(combi + [False])
                else: # ()가 없다면 -> ()가 있거나 ()가 없는 경우가 존재
                    que.append(combi + [False])
                    que.append(combi + [True])
        ### 연산 수행하기
        result = (-2)**31 + 1
        for combi in combinations:
            # print("="*30)
            # print("조합식 >>", combi)
            numbers = copy.deepcopy(original_numbers)
            operators = copy.deepcopy(original_operators)
            ### () 인덱스 찾기
            true_idxs = []
            for idx, x in enumerate(combi):
                if x: true_idxs.append(idx)
            ### () 먼저 연산
            for true_idx in true_idxs:
                operator = operators[true_idx]

                if operator == "+":
                    value = numbers[true_idx] + numbers[true_idx + 1]
                elif operator == "-":
                    value = numbers[true_idx] - numbers[true_idx + 1]
                elif operator == "*":
                    value = numbers[true_idx] * numbers[true_idx + 1]

                numbers[true_idx] = value
                numbers[true_idx + 1] = None
                operators[true_idx] = None
            ### 연산식 찾기
            new_numbers, new_operators = deque(), deque()
            for i in range(len(numbers)):
                if numbers[i] is not None:
                    new_numbers.append(numbers[i])
            for i in range(len(operators)):
                if operators[i] is not None:
                    new_operators.append(operators[i])
            # print("최종 연산식")
            # print(new_numbers)
            # print(new_operators)
            ### 연산하기
            value = new_numbers.popleft()
            while new_operators:
                operator = new_operators.popleft()

                if operator == "+":
                    value += new_numbers.popleft()
                elif operator == "-":
                    value -= new_numbers.popleft()
                elif operator == "*":
                    value *= new_numbers.popleft()

            result = max(result, value)

        print(result)
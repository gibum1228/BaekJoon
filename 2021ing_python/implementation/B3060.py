import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    see = {
        1: [2, 4, 6], 2: [1, 3, 5], 3: [2, 4, 6],
        4: [3, 5, 1], 5: [4, 6, 2], 6: [5, 1, 3]
    }

    for _ in range(int(IN())): # test case 입력 받기
        N = int(IN())
        pigs = list(map(int, IN().split()))
        count = 1
        food_sum = sum(pigs)

        while True:
            if food_sum > N: break

            new_pigs = []
            new_food_sum = 0
            for now_num in range(1, 7):
                food_want = pigs[now_num - 1]

                for near_num in see[now_num]:
                    food_want += pigs[near_num - 1]

                new_pigs.append(food_want)
                new_food_sum += food_want

            count += 1
            pigs = new_pigs
            food_sum = new_food_sum

        print(count)
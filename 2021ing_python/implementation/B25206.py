import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    score = {
        k: v for k, v in zip(['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F'], [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0])
    }

    sum_b = 0
    sum_c = 0
    for _ in range(20):
        a, b, c = IN().rstrip().split(' ')
        b = float(b)

        if c != 'P':
            sum_b += b
            sum_c += (b * score[c])

    print(sum_c / sum_b)
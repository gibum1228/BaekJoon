if __name__ == "__main__":
    N = int(input())
    result = 0
    i = 1

    while True:
        num = pow(10, i)

        a = N // num
        b = N % num

        if a == 0:
            result += ((b - pow(10, i-1)) + 1) * i
            break
        else:
            if i == 1:
                result += 9
            else:
                result += pow(10, i-1) * i * 9

        i += 1

    print(result)
if __name__ == "__main__":
    N = int(input())

    line, num = 0, 0
    while N > num:
        line += 1
        num += line
    
    gap = num - N

    if line % 2 == 0:
        top = line - gap
        bottom = gap + 1
    else:
        top = gap + 1
        bottom = line - gap
    
    print(f"{top}/{bottom}")
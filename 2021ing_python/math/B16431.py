if __name__ == "__main__":
    br, bc = map(int, input().split())
    dr, dc = map(int, input().split())
    jr, jc = map(int, input().split())

    # bessie
    b_weight = max(abs(jr - br), abs(jc - bc))

    # daisy
    d_weight = abs(jr - dr) + abs(jc - dc)

    if b_weight < d_weight:
        print("bessie")
    elif d_weight < b_weight:
        print("daisy")
    else:
        print("tie")
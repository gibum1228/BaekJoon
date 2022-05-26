import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    sh, sm, ss = map(int, IN().split(" : "))
    eh, em, es = map(int, IN().split(" : "))

    st = sh * 3600 + sm * 60 + ss
    et = eh * 3600 + em * 60 + es

    print(et - st if et >= st else et - st + (3600 * 24))
import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    context = IN().rstrip()
    search_word = IN().rstrip()

    count = 0
    i = 0
    while i < len(context):
        if search_word == context[i:i+len(search_word)]:
            i += len(search_word)
            count += 1
        else:
            i += 1

    print(count)
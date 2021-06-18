def swap(a, b):
    return b, a

inputs = list(map(int, input().split()))

while True:
    if inputs[0] > inputs[1]:
        inputs[0], inputs[1] = swap(inputs[0], inputs[1])
        print(" ".join(list(map(str, inputs))))
    if inputs[1] > inputs[2]:
        inputs[1], inputs[2] = swap(inputs[1], inputs[2])
        print(" ".join(list(map(str, inputs))))
    if inputs[2] > inputs[3]:
        inputs[2], inputs[3] = swap(inputs[2], inputs[3])
        print(" ".join(list(map(str, inputs))))
    if inputs[3] > inputs[4]:
        inputs[3], inputs[4] = swap(inputs[3], inputs[4])
        print(" ".join(list(map(str, inputs))))

    if inputs == [1, 2, 3, 4, 5]:
        break

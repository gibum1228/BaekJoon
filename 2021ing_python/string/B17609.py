import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    T = int(IN())
    strings = [IN().rstrip() for _ in range(T)]
    results = []

    for string in strings:
        left, right = 0, len(string)-1
        trigger = True
        two_trigger = True
        # print("="*5, string, "="*5)
        while left <= right:
            # print(left, right, string[left], string[right])
            if string[left] == string[right]:
                left += 1
                right -= 1
            else:
                # 유사 회문
                if two_trigger and ((string[left + 1] == string[right]) or (string[left] == string[right - 1])):
                    # 한 번을 건너 봤을 때 뭘 삭제해도 동일하다면 두 번 넘어까지 봐야 함
                    if (string[left + 1] == string[right]) and (string[left] == string[right - 1]):
                        copy_left, copy_right = left + 1, right
                        del_left = True

                        while copy_left < copy_right:
                            if string[copy_left] == string[copy_right]:
                                copy_left += 1
                                copy_right -= 1
                            else:
                                del_left = False
                                break
                    else:
                        del_left = True if string[left + 1] == string[right] else False

                    if del_left:
                        left += 2
                        right -= 1
                    else:
                        left += 1
                        right -= 2

                    two_trigger = False
                else: # 회문, 유사 회문 둘 다 아님
                    trigger = False
                    results.append(2)
                    break

        if trigger:
            results.append(0 if two_trigger else 1)

    print(*results, sep='\n')
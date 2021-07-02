'''
int(str, #)
#: 2, 8, 16
'''
value = int(input(), 2)

'''
매개변수 값은 10진수
bin(), oct(), hex()
'''
print(oct(value).split('0o')[1])
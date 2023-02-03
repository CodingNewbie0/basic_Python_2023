# 좀 더 복잡한 계산기
a = int(input('계산할 첫번째 정수를 입력하세요. : '))
b = int(input('계산할 두번째 정수를 입력하세요. : '))

def calc(option, *args):
    result = 0
    if option == 'add':
        for i in args:
            result += i
    
    elif option == 'mul':
        result = 1
        for i in args:
            result *= i

    elif option == 'sub':
        result = args[0]
        for i in args[1:]:
            result -= i

    elif option == 'div':
        result = args[0]
        for i in args[1:]:
            result /= i

    elif option == 'namuzi':
        result = args[0]
        for i in args[1:]:
            result %= i

    return result

# print(calc('add', 4, 7, 17))
# print(calc('mul', 512, 2, 4, 2))
# print(calc('sub', 10 ,248, 396))
# print(calc('div', 100, 5))

print('두 수를 더한 값 : ', calc('add', a, b))
print('두 수를 뺀 값 : ', calc('sub', a, b))
print('두 수를 곱한 값 : ', calc('mul', a, b))
print('두 수를 나눈 값 : ', calc('div', a, b))
print('두 수의 몫 : ', calc('namuzi', a, b))

def new_calc(x, y):
    return (x*y, x/y, x+y, x-y)

# 받을때는 튜플(소괄호) 생략가능
# (res1, res2, res3, res4) = new_calc(5, 7)
# res1, res2, res3, res4 = new_calc(5, 7)
# print(res1, res2, res3, res4)


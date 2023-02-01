# 전역/지역변수
num = 1

for i in range(1, 10):
    num = i * num
    print(f'{i + 1}번\n')

    if i % 3 == 0: # 3의 배수
        res = '테스트\n'
        print(res)

print(f'결과 {num}\n')
print(res)
# 다중입력

# x, y = input('두 영단어를 입력하세요 - > ').split(' ')

# print(x, y)
# print(y)

# 완전 다중입력(개수가 몇개든지 상관없음)
inputs = list(map(int, input('정수를 입력하세요 : ').split()))
print(f'{inputs}')

inputs2 = list(map(str, input('단어를 입력하세요 : ').split()))
print(f'{inputs2}')

# a = input('안녕\n')
# if a == 'ㅎㅇ':
#     print('나도안녕')
# elif a == 'ㅎㅇㅎㅇ':
#     print('ㅎㅇㅎㅇㅎㅇㅎㅇㅎㅇㅎㅇㅎㅇㅎㅇㅎㅇㅎㅇ')
    
# elif a == '':
#     print('왜 아무말도안함')
# else:
#     print('?')
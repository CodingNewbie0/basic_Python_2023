# if문

name = input('당신의 이름은? : ')
if name == '효창':
    print('빈자리로 간다.')
elif name == '장후':
    print('예약석으로 간다.')
else:
    print('기다린다.')

a = int(input('수를 입력하시오 : '))
b = int(input('수를 입력하시오 : '))
if a < b:
    print('a는 b보다 작다.')
elif a == b:
    print('a는 b와 같다.')
else:
    print('a는 b보다 크다.')
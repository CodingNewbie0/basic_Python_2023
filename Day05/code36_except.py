# 예외처리
def add(a, b):
    return a + b
    
def mul(a, b):
    return a * b
    
def div(a, b):
    return a / b

try:
    x, y = input('두 수를 입력하세요 : ').split()
    x = int(x)
    y = int(y)
except Exception as e:
    print(e)
    exit() # exit을 넣으면 무조건 코드가 여기서 끝남
finally:
    print('계산오류!') # exit 넣어서 끝내도 finally까지 실행하고 종료됨

# 매우 원시적인 방법. 
# if y == 0:
#     print('y에 0을 넣지마세요.')
#     exit() # exit을 넣으면 무조건 코드가 여기서 끝남

print('계산 테스트')
try:
    print(f'나누기 : ', div(x, y))
# except ZeroDivisionError as e:
#     print('0으로 나누면 안됩니다.') # 개발할때 굳이 쓸 이유가 없음. 나만 피곤함.
except Exception as e: # Exception은 모든 예외처리를 해줌. 그리고 예외처리에서 제일 마지막에 들어가야됨.
    print(e)
finally:
    print('계산은 계속됩니다.')

print(f'더하기 : ', add(x, y))
print(f'곱하기 : ', mul(x, y))

# 함수
# 함수정의 - 실행X
# 함수 만드는 방법 4가지
# 1. 파라미터 0 리턴 0
# 2. 파라미터 0 리턴 X
# 3. 파라미터 X 리턴 0
# 4. 파라미터 X 리턴 X
def add(x, y):
    result = x + y 
    print(result)

def sub(x, y):
    result = x - y
    print(result)

def mul(x, y):
    result = x * y
    print(result)

def div(x, y):
    result = x // y
    print(result)

def mok(x, y):
    result = x % y
    print(result)

def hello():
    print('Hello~!!!')

def hello2():
    msg = 'Hello, Hello'
    return msg

# 함수호출
val = add(1024, 5)
print(val)

val = sub(1024, 100)
print(val)

val = mul(1024, 2)
print(val)

val = div(1024, 512)
print(val)

val = mok(1024, 37)
print(val)

hello()
result = hello2
print(result)
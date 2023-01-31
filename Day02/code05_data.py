# 자료형
# None : 값이 없는 값
None # 컴퓨터 : ㅁ?ㄹ

print(None)
print(0 == None)
print('' == None)

# 숫자형
val = 3
print(type(val))

val = 3.14
print(type(val))

val = 'Hello'
print(type(val))

val = 0b1010
print(type(val))

val = 12.124124423
print(type(val))

val = 4_520_000
print(type(val))

val = 3_099.99
print(type(val))

# 문자열
val = 'Life is short, You need Python.'
print(val)
print(type(val))

val = 'Hell\nworld!' # 탈출문자(한줄내리기)
print(val)

val = 'Hell\tWorld!' # 탭
print(val)

val = 'Hell\t\bWorld!' # 백스페이스(한칸앞으로)
print(val)

val = '''Life is short, 
You need Python.'''
print(val)

val = "Hi, i'm 'hc'"
print(val)
val = 'Hi, i\'m \'hc\''
print(val)

# 불링형 or 불형
참 = True
거짓 = False

print(1+1==1)
a = 1
b = 2
print(a+b == 3)
# 거짓이라는 False 값 변수가 참인지 거짓인지 판별
print(거짓 == True)
print(거짓 == False)
print(참 is True)
print(참 is False)

print(bool(1)) # 1 == True
print(bool(0)) # 0 == False
print(bool(3)) # 1이상의 값은 모두 참이지만 쓰지않고, 0과 1로 참 거짓을 구분한다.

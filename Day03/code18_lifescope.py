# 라이프스코프
a = 1

def vartest(x):
    x = x + 1
    return x

a = vartest(a)
print(a)

a = 1 
def vartest():
  global a # 전역(모든곳)에 있는 a를 함수(지역)에서 가져다 씀
  a = a + 1

vartest()
print(a)
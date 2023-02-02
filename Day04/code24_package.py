# 패키지
import math as m # 클래스로 안된 모듈
import code22_person as p # 내가 만든 클래스(모듈)
from code23_car import Car # 모듈 안의 특정 클래스를 가져다 씀

print(m.pi)
print(m.ceil(2.1)) # 반올림(무조건 올림)
print(m.sqrt(4))
print(m.pow(2, 10)) # 지수함수

# 내가 만든 모듈 사용
me = p.Person('강복순', 155, '여성')
print(me)

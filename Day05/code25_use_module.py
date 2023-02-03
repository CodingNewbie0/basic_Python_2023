# 모듈사용
import random

# print(random.choice(range(1, 7)))
numbers = [i for i in range(1, 100)] # 1~45 리스트
gacha = []

for i in range(10):
    gacha.append(random.choice(numbers))

print(gacha)

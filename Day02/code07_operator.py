# 연산자
# 할당연산 assignment
# 2 = 1 (X)
val = 1

# equal 연산자
print(1 == 1)

# 사칙연산
print(1 + 1)
print(10 * 10)
print(1024 / 2) # 소수나누기
print(1024 // 2) # 정수나누기
print(6 // 3)
print(6 % 3) # 몫 3->0 6->0 9->0

# print(6 / 0) 무한대 값은 컴퓨터가 표현할 방법이 없음.
# print(6 // 0)

print(2 ** 10)

# 문자열연산
first = 'Hello'
second = 'World'
print(first + second)
print(first + '\t\b\b' + second)
print(first, second)

print(first * 4)

# 문자열길이
print(len(first))
print(first[0])
print(first[1])
print(first[2])
print(first[3])
print(first[4])
# print(first[5]) Index 에러

print(first[-1])
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])

# 리스트 자르기전
current = '2023-01-31 15:14:02 # 현재시간'
print(len(current))
print(current[0:4])
print(current[5:7])
print(current[8:10])
print(current[11:13])
print(current[14:16])
print(current[17:])

print(len(current))
print(current[0:4] + '년' + current[5:7] + '월' + current[8:10] + '일' +
      current[11:13] + '시' + current[14:16] + '분' + current[17:19] + '초' + current[19:])


# 리스트 연산
que = [1,2,3,4,5]
que[0] = 7
print(que)

que.append(10) # 값이 맨 마지막에 추가
print(que)

que.insert(3, 99) # 특정 인덱스에 값 추가
print(que)

que.remove(10) # 특정값이 삭제
print(que)

tup = [1,2,3,4,5]
# tup[1] = 9 튜플은 수정불가능 오류남.
print(tup)

# 문자열 == 문자 리스트
title = 'python'
print(title)

# title[0] = 'P' 문자열에서는 값변경이 불가능
print('P' + title[1:])

# 일반적인 문자형 리스트
text = ['p', 'y', 't', 'h', 'o', 'n']
print(text)
text[0] = 'P'
print(text)

# 문자열 포맷팅(구식)
print("I'm so happy {0} you!! {1}".format(2, 'WOW~'))
# 최신식 문자열 포맷팅
preword = 2
sayHello = 'WOW!!'
print(f"I'm so happy {preword} you!! {sayHello}")

pi = 3.1415927
print(f"파이는 {pi}입니다.")
print(f"파이는 {pi:0.2f}입니다.") # 소숫점의 숫자 자리수까지 출력
print(f"파이는 {pi:10.2f}입니다.") # 정수 숫자 자리수까지 공간을 띄움

name = 'HyoChang. Park'
vals = name.split() # 스페이스
print(type(vals))
print(vals)

vals = name.split('.') # .으로 지정
print(vals)

print(name.replace('HyoChang.', 'Tomas')) # 문자열에서 특정단어를 바꿈

# 문자열 공백 없애기
hi = '               ok bye~            '
print(hi.lstrip() + '|') # 왼쪽공백 X
print(hi.rstrip() + '|') # 오른쪽공백 X
print(hi.strip() + '|') # 양쪽공백 X

# 문자열에서 값 찾기
print(name.index('C')) # 단어의 시작위치를 알려줌

print(name.find('G')) # 찾는 값이 없으면 -1
print(name.find('a'))

print(name.count('a')) # 찾는 값의 갯수

# 모든 단어를 대문자/소문자로 변경
print(name.upper())
print(name.lower())

# 연산자 우선순위
print(3 + 4 * 2)
print((3 + 4) * 2)

# 괄호우선 -> 연산문자 -> 객체문자


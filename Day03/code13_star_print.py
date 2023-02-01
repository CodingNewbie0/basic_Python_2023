# 별표찍기
for star in range(1, 6, 1): # 1부터 5까지 1씩 증가 반복
  print('*'*star)

# 별표찍기
for star in range(5, 0, -1): # 5부터 1까지 1씩 감소 반복
  print('*'*star)
# 순서대로 별찍기
x = int(input('줄 수를 입력하세요 : '))
for star in range(1, x+1):
  for star2 in range(star):
    print('*', end="")
  print()

# 반대로 별찍기
x = int(input('줄 수를 입력하세요 : '))
for star in range(1, x+1):
  for star2 in range(x+1 - star):
    print('*', end="")
  print()
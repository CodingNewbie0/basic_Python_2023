# while문
hit = 0 # 변수 초기화

while hit < 10001: # while true는 무한반복 오류날수도 있으니 조심해서 쓸것.
    hit += 1

    print(f'나무를 {hit:2d}번 찍었습니다.')
    if hit == 10:
        print('나무가 넘어갑니다.')
        break
    else:
        print('나무가 아직 넘어가지 않았습니다.\n')

print('\n나무찍기를 마칩니다.')

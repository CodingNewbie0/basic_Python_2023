# 무한반복 예제
num = 0

while True:
    print('''\n처리할 메뉴번호를 입력하세요.\n
1. 회원입력
2. 회원검색
3. 회원수정
4. 회원삭제
5. 종료\n
번호 입력 : ''', end="")
    num = int(input())

    if num == 1:
        print('\n회원입력')
    elif num == 2:
        print('\n회원검색')
    elif num == 3:
        print('\n회원수정')
    elif num == 4:
        print('\n회원삭제')
    elif num == 5:
        break
    else:
        print('\n해당하는 숫자는 없는 숫자입니다. 다시 입력해주세요.')
        continue
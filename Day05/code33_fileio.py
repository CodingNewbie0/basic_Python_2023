# 파일 만들기
file = open('sample.txt', 'w', encoding='utf-8') # 파일을 쓰기로 만듦
# r = 읽기모드, 파일을 읽어올때 사용
# w = 쓰기모드, 파일에 내용을 쓸때 사용
# a = 추가모드, 파일에 내용을 추가할 때 사용
# b = 이진모드
# t = 텍스트모드, 기본값으로 사용하지 않아도 됨
# U = 유니버설 개행모드 (사용되지 않음)
# + = 업데이트(읽기 및 쓰기)를 위한 디스크 파일 열기

# ASCII -> 한 단어를 표현하는 체계(영어)
# Unicode(UTF-8) -> 모든 나라언어를 다 표현가능

file.write('안녕하세요.\n')
file.write('저는 파일입니다.\n')
file.write('경로에 파일이 생성됩니다.\n')

file.close()
print('sample.txt가 생성되었습니다.')


# 파일/폴더 경로
# 절대경로 : 최상위 디렉토리가 반드시 포함된 경로
file = open('C:/DEV/Temp/Bank/sample01.txt', 'w', encoding='utf-8') # 파일을 쓰기로 만듦

file.write('안녕하세요.\n')
file.write('저는 파일입니다.\n')
file.write('절대경로에 파일이 생성됩니다.\n')

file.close()
print('sample01.txt가 생성되었습니다.')

# 상대경로 : 현재 디렉토리(비교 대상)를 기준으로 작성된 경로
# . : 현재폴더, .. : 부모폴더(현재폴더 들어오기전 폴더)
file = open('./Day05/sample02.txt', 'w', encoding='utf-8') # 파일을 쓰기로 만듦

file.write('안녕하세요.\n')
file.write('저는 파일입니다.\n')
file.write('상대경로에 파일이 생성됩니다.\n')

file.close()
print('sample02.txt가 생성되었습니다.')
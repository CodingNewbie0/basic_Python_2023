# 외부 패키지 사용
import requests

url = input('주소를 입력하세요. : ') #  https://www.naver.com
res = requests.get(url)
print(res.status_code)
print('===============')
print(res.content)
# 객체지향
class Person:
    name = '이름'
    height = '키'
    weight = '무게'
    gender = '성별'
    blood_type = '혈액형'

# 1. 생성자 추가
    def __init__(self):
        self.name = '홍길동'
        self.height = '170'
        self.weight = '80'
        self.gender = 'male'
        self.blood_type = 'AB'

    def __init__(self, name = '홍길동', height = 170, gender = 'male' , blood_type = 'AB') -> None:
        self.name = name
        self.height = height
        self.gender = gender
        self.blood_type = blood_type

    def walk(self):
        print(f'{self.name}이(가) 걷습니다.')

    def run(self, option):
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빨리 뜁니다!')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다~')

    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')

# 2. 생성자외 매직메서드(function) __str__
    def __str__(self) -> None:
        return (f'이름은 {self.name}, 성별은 {self.gender} 입니다.')

hyochang = Person('박효창','RH+ A') # 객체생성을 instance(예)라 명시
# hyochang.name = '박효창'
# hyochang.height = '180'
# hyochang.weight = '73'
# hyochang.gender = 'male'
# hyochang.blood_type = 'RH+ A'

# print(f'제 이름은 {hyochang.name} 입니다.')
# print(f'키는 {hyochang.height}cm 입니다.')
# print(f'무게는 {hyochang.weight}kg 입니다.')
# print(f'성별은 {hyochang.gender} 입니다.')
print(f'{hyochang.name}의 혈액형은 {hyochang.blood_type} 입니다.')

hyochang.run('Fast')

# 1. 초기화 후 객체생성
hong = Person()
hong.run('Slow')
print(hong)

print('======================================')
# 2. 파라미터를 받는 생성자 실행
ashely = Person('애슐리', 160, 45, 'female')
print(ashely.name)
print(ashely.height)
print(ashely.weight)
print(ashely.gender)
print(ashely.blood_type)
print(ashely)
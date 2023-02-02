# 객체지향
class Person:
    name = '이름'
    height = '키'
    weight = '무게'
    gender = '성별'
    blood_type = '혈액형'

    def walk(self):
        print('걷습니다.')

    def run(self, option):
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빨리 뜁니다!')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다~')
    

hyochang = Person() # 객체를 instance(예)라 명시
hyochang.name = '박효창'
hyochang.height = '180'
hyochang.weight = '73'
hyochang.gender = 'male'
hyochang.blood_type = 'RH+ A'

print(f'제 이름은 {hyochang.name} 입니다.')
print(f'키는 {hyochang.height}cm 입니다.')
print(f'무게는 {hyochang.weight}kg 입니다.')
print(f'성별은 {hyochang.gender} 입니다.')
print(f'혈액형은 {hyochang.blood_type} 입니다.')
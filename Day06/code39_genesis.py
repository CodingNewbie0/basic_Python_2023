# Car클래스를 상속한 제네시스 클래스
from code38_car import Car

# Child class
class Genesis(Car):
    def __init__(self, name, color, plate_number, product_year) -> None:
        super().__init__()

        self.__name = name
        self.__color = color
        self.__plate_number = plate_number
        self.__product_year = product_year
        print(f'{self.__name} 인스턴스 생성!')

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name # 한번 더 재정의 해줘야 부모클래스에 있는 이름을 가져오지 않음.

    def run(self):
        return f'{self.__name}이(가) 달립니다.'

    def stop(self):
        return f'{self.__name}이(가) 멈춥니다.'

gv80 = Genesis('팔공이', 'black', '66오 1004', 2022)
# gv80.set_name('팔공이')
print(f'이 차의 이름은 {gv80.get_name()}입니다.')
print(gv80.run())
print(gv80.stop())

# 다중상속 : 하나의 자식클래스가 하나 이상의 부모클래스의 유산을 물려받는다는 것
# 메서드재정의(오버라이딩) : 메서드 재정의는 부모클래스의 메서드를 자식클래스에서 다시 재정의 하는 것
# 정적메서드 : 클래스에서 직접 접근할 수 있는 메소드
# 추상클래스 : 이름만 존재하고 메서드 구현이 없는 클래스

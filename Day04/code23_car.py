# 자동차 클래스
class Car:
    __number = '12가 3456'
    name = '그렌져'

    def get_number(self):
        return self.__number

    # 클래스 외부에선 변경X, 멤버함수로는 내부에서 변경O
    def set_number(self, number):
        self.__number = number

    def __init__(self, number = '888호 8888'): # __init__ 메서드를 생성(불러옴)<제일 자주씀>
        self.__number = number
        print('__init__')

    # def __new__(cls: type[Self]) -> Self:
    #     print('__new__')
    #     return super().__new__(cls) # 부모클래스(상속)

    def __str__(self) -> str:
        return f'차번호는 {self.__number}'
    
yourcar = Car('00라 1265')
print(yourcar)
yourcar.__number = '74우 5471' # 외부에서는 멤버변수에 접근불가
print(yourcar)
print('클래스 내부함수 사용!')
yourcar.set_number('55오 5555')
print(yourcar)

mycar = Car()
print(mycar)
print(f'차는 {mycar.name}고 번호는 {mycar.get_number()}')

mycar.__number = '765하 4321'
print(f'차는 {mycar.name}고 번호는 {mycar.get_number()}')
print(mycar.get_number())
print(mycar)
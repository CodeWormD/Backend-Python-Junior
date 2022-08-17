from os import stat_result
import string
from typing import Union

# First
class Alphabet():
    def __init__(self, lang, letters_str):
        self.lang = lang
        self.letters = letters_str
    
    def show(self):
        print(f'{self.letters}')
        
    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):

    __letters_num = 26

    def __init__(self, lang, letters):
        super().__init__(lang, letters)
        self.lang = lang
        self.letters = list(letters)

    def is_en_letter(self, letter):
        return True if letter.upper() in self.letters else False
    
    def letter_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        return ('SOME ENGLISH TEXT I GUESS')


# if __name__ == '__main__':
    
    # alp = EngAlphabet('En', string.ascii_uppercase)
    # alp.show()
    # print(alp.letter_num())
    # print(alp.is_en_letter('A'))
    # print(alp.is_en_letter('Г'))
    # print(alp.example())



# Purchase the house
class Human():
    
    _default_name = 'No name'
    _default_age = 0
    
    def __init__(self, name=_default_name, age=_default_age, ):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None
    
    def info(self):
        print (f'Имя: {self.name}, Возраст: {self.age}, Дом: {SmallHouse.default_name}, Деньги: {self.__money}')
    
    @staticmethod
    def default_info():
        print (f'Имя: {Human._default_name}, Возраст: {Human._default_age}')
    
    def earn_money(self, salary: int):
        self.__money += salary
        print(f'Earned - {salary}. Total money: {self.__money}')
    
    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money > price:
            self.__make_deal(house, price)
        else:
            print('Not enough money')

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house


class House():
    def __init__(self, _area: int, _price: int, _name: str) -> Union[int, str]:
        self._area = _area
        self._price = _price
        self._name = _name
    
    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        return final_price


class SmallHouse(House):
    
    default_area = 40
    default_price = 1000
    default_name = 'Tiny house'
    
    def __init__(self):
        super().__init__(
            SmallHouse.default_area,
            SmallHouse.default_price,
            SmallHouse.default_name)


if __name__ == '__main__':
    Human.default_info()
    
    pasha = Human('Pasha', 25)
    pasha.info()
    
    tiny_house = SmallHouse()
    
    pasha.buy_house(tiny_house, 1)
    pasha.earn_money(1500)
    pasha.buy_house(tiny_house, 1)
    pasha.info()
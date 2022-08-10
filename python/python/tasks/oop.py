from os import stat_result
import string

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


if __name__ == '__main__':
    
    alp = EngAlphabet('En', string.ascii_uppercase)
    alp.show()
    print(alp.letter_num())
    print(alp.is_en_letter('A'))
    print(alp.is_en_letter('Г'))
    print(alp.example())



# Purchase the house
class Human():
    
    default_name = 'No name'
    default_age = 0
    
    def __init__(self, name=default_name, age=default_age, ):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None
    
    def info(self):
        return (f'{self.name}, {self.age}, {self._house}, {self._money}')
    
    @staticmethod
    def default_info():
        return (f'{Human._default.name}, {Human._default.age}')
    
    def earn_money(self, salary):
        self.__money += salary
        print(f'Earned - {salary}. Total money: {self.__money}')
    
    def buy_house(self):
        pass

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house
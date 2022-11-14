

class Soda:

    def __init__(self, add=None):
        self.add = add

    def show_my_drink(self):
        if isinstance(self.add, str):
            print(f'Газировка и {self.add}')
        else:
            print('Обычная газировка')

# a = Soda()
# b = Soda('вишня')
# c = Soda(5)
# cc = Soda('малина')
# a.show_my_drink()
# b.show_my_drink()
# c.show_my_drink()
# cc.show_my_drink()
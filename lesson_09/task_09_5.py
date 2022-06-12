class Stationery:

    def __init__(self):
        self.title = 'title'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self):
        super().__init__()
        self.title = 'Ручка'

    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):

    def __init__(self):
        super().__init__()
        self.title = 'Карандаш'

    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):

    def __init__(self):
        super().__init__()
        self.title = 'Маркер'

    def draw(self):
        print('Запуск отрисовки маркером')


pen_1 = Pen()
pen_1.draw()
pencil_1 = Pencil()
pencil_1.draw()
handle_1 = Handle()
handle_1.draw()

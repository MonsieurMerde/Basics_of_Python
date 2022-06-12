class Worker:
    name = 'John'
    surname = 'Smith'

    def __init__(self, wage, bonus):
        self.position = 'engineer'
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, wage, bonus):
        super().__init__(wage, bonus)

    def get_full_name(self):
        return f'Name: {self.name}\nSurname: {self.surname}'

    def get_total_income(self):
        return f'Total income: {self._income["wage"] + self._income["bonus"]}'


eng_1 = Position(50000, 10000)
print(eng_1.name)
print(eng_1.surname)
print(eng_1.position)
print(eng_1._income)
print(eng_1.get_full_name())
print(eng_1.get_total_income())

eng_2 = Position(100000, 30000)
print(eng_2.name)
print(eng_2.surname)
print(eng_2.position)
print(eng_2._income)
print(eng_2.get_full_name())
print(eng_2.get_total_income())

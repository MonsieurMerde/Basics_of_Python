class Cell:

    def __init__(self, cell_amt):
        if type(cell_amt) != int:
            raise TypeError('The number of cells must be int')
        if cell_amt < 0:
            raise ValueError('The number of cells must be greater than or equal to 0')
        self.cell_amt = cell_amt

    def __add__(self, other_cell):
        return Cell(self.cell_amt + other_cell.cell_amt)

    def __sub__(self, other_cell):
        if self.cell_amt <= other_cell.cell_amt:
            raise ValueError('The number of cells in the second cell must be less than the number of cells in the first cell')
        else:
            return Cell(self.cell_amt - other_cell.cell_amt)

    def __mul__(self, other_cell):
        return Cell(self.cell_amt * other_cell.cell_amt)

    def __floordiv__(self, other_cell):
        if other_cell.cell_amt == 0:
            raise ZeroDivisionError('The number of cells in the second cell is 0')
        if self.cell_amt <= other_cell.cell_amt:
            raise ValueError('The number of cells in the second cell must be less than the number of cells in the first cell')
        else:
            return Cell(self.cell_amt // other_cell.cell_amt)

    def make_order(self, cell_amt_in_row):
        if cell_amt_in_row <= 0:
            raise ValueError('The number of cells in a row must be greater than 0')
        cell_amt_counter = self.cell_amt
        cell_str = ''
        while True:
            if cell_amt_counter <= cell_amt_in_row:
                cell_str += '*' * cell_amt_counter
                break
            cell_str += '*' * cell_amt_in_row + '\n'
            cell_amt_counter -= cell_amt_in_row
        return cell_str


cell_1 = Cell(1)
print(type(cell_1))
print(cell_1.make_order(5))
cell_2 = Cell(5)
print(type(cell_2))
print(cell_2.make_order(2))
cell_3 = Cell(0)
print(type(cell_3))
print(cell_3.make_order(5))
cell_4 = Cell(27)
print(type(cell_4))
print(cell_4.make_order(6))
cell_5 = Cell(11)
print(type(cell_5))
print(cell_5.make_order(11))
cell_6 = cell_2 + cell_5
print(type(cell_6))
print(cell_6.make_order(2))
cell_7 = cell_4 - cell_1
print(type(cell_7))
print(cell_7.make_order(4))
cell_8 = cell_2 * cell_4
print(type(cell_8))
print(cell_8.make_order(40))
cell_9 = cell_8 // cell_2
print(type(cell_9))
print(cell_9.make_order(10))


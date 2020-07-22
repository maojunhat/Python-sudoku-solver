import json


class Sudoku:
    def __init__(self):
        with open('sudokus.json', 'r') as f:
            self.sudoku = json.load(f)

    @staticmethod
    def tile_at(row_number, column_number):
        """

        :param row_number:
        :param column_number:
        :return: subscript of this tile in list sudoku
        """
        return row_number * 9 + column_number

    def has_same_in_row(self, attempt, subscript):
        row_number = int(subscript / 9)
        values = [
            self.sudoku[self.tile_at(row_number, column_number)]
            for column_number in range(9)
        ]
        if attempt in values:
            return True
        else:
            return False

    def has_same_in_column(self, attempt, subscript):
        column_number = int(subscript % 9)
        values = [
            self.sudoku[self.tile_at(row_number, column_number)]
            for row_number in range(9)
        ]
        if attempt in values:
            return True
        else:
            return False

    def has_same_in_big_block(self, attempt, subscript):
        row_begin_number = int(int(subscript / 9) / 3) * 3
        column_begin_number = int(int(subscript % 9) / 3) * 3
        values = [
            self.sudoku[self.tile_at(row, column)]
            for row in range(row_begin_number, row_begin_number + 3)
            for column in range(column_begin_number, column_begin_number + 3)
        ]
        if attempt in values:
            return True
        else:
            return False

    def is_suitable(self, attempt, subscript):
        is_not_suitable = self.has_same_in_row(attempt, subscript) \
                          or self.has_same_in_column(attempt, subscript) \
                          or self.has_same_in_big_block(attempt, subscript)
        return not is_not_suitable

    def solve_sudoku(self, subscript=-1):
        if subscript == -1:
            subscript = self.find_next_blank()
        for attempt in range(1, 10):
            if self.is_suitable(attempt, subscript):
                self.sudoku[subscript] = attempt
                next_subscript = self.find_next_blank(subscript)
                if next_subscript == -1 or self.solve_sudoku(next_subscript):
                    return True
        self.sudoku[subscript] = 0
        return False

    def find_next_blank(self, subscript=0):
        while self.sudoku[subscript] != 0:
            subscript += 1
            if subscript >= 81:
                return -1
        return subscript

    def show_sudoku(self):
        my_str = ''
        for row in range(9):
            for column in range(9):
                my_str += str(self.sudoku[self.tile_at(row, column)])
                my_str += ' '
            my_str += '\n'
        print(my_str)

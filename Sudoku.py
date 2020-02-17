import copy


class Sudoku:
    def __init__(self, board):
        self.board = board[:]

    def print_board(self):
        for line in self.board:
            print(line)
        print()

    def print_board_zeros(self):
        for row in self.board:
            for num in row:
                if type(num) == list:
                    print(0, end=" ")
                else:
                    print(num, end=" ")
            print()
        print()

    def del_row_pos(self, row_num, possibility):
        for x, num in enumerate(self.board[row_num]):
            if type(num) == list:
                if possibility in num:
                    self.board[row_num][x].remove(possibility)

    def del_column_pos(self, column_num, possibility):
        for row in self.board:
            num = row[column_num]
            if type(num) == list:
                if possibility in num:
                    num.remove(possibility)

    def del_box_pos(self, box_row, box_column, possibility):
        for row_num in range(3):
            for column_num in range(3):
                num = self.board[box_row * 3 + row_num][box_column * 3 + column_num]
                if type(num) == list:
                    if possibility in num:
                        num.remove(possibility)

    def check_row_unique(self, row_num, column_num):
        for possibility in self.board[row_num][column_num]:
            count = -1
            for other_num in self.board[row_num]:
                if type(other_num) == list:
                    if possibility in other_num:
                        count += 1
                elif other_num == possibility:
                    count += 1
            if count == 0:
                self.board[row_num][column_num] = possibility
                return

    def check_column_unique(self, row_num, column_num):
        num = self.board[row_num][column_num]
        for possibility in num:
            count = -1
            for other_slot_num in range(0, 9):
                other_slot = self.board[other_slot_num][column_num]
                if type(other_slot) == list:
                    if possibility in other_slot:
                        count += 1
                elif other_slot == possibility:
                    count +=1
            if count == 0:
                self.board[row_num][column_num] = possibility
                return

    def check_box_unique(self, row_num, column_num, block_row, block_column):
        num = self.board[row_num][column_num]
        for possibility in num:
            count = -1
            for x in range(0, 3):
                for y in range(0, 3):
                    other_row = 3 * block_row + x
                    other_column = 3 * block_column + y
                    other_slot = self.board[other_row][other_column]
                    if type(other_slot) == list:
                        if possibility in other_slot:
                            count += 1
                    elif other_slot == possibility:
                        count += 1
            if count == 0:
                self.board[row_num][column_num] = possibility
                return

    def solve(self):
        all_filled = True # Will be set false if there are any lists
        for row_num, row in enumerate(self.board):
            for column_num, num in enumerate(row):
                if num == 0:
                    self.board[row_num][column_num] = list(range(1, 10))

        board_filled = False
        while not board_filled:
            all_filled = True # will be set false if the program finds any list of possible nums
            for box_row in range (0, 3):
                for box_column in range(0, 3):
                    for sub_row in range (0, 3):
                        for sub_column in range(0, 3):
                            row_num = box_row * 3 + sub_row
                            column_num = box_column * 3 + sub_column
                            num = self.board[row_num][column_num]
                            if type(num) == list and len(num) == 1: # There is only one possibility for this slot
                                self.board[row_num][column_num] = num[0]
                                num = self.board[row_num][column_num]
                            if type(num) == int:
                                self.del_row_pos(row_num, num)
                                self.del_column_pos(column_num, num)
                                self.del_box_pos(box_row, box_column, num)
                            else:
                                all_filled = False # A list was found, all positions are not filled
                                self.check_row_unique(row_num, column_num)
                                if type(self.board[row_num][column_num]) == list:
                                    self.check_column_unique(row_num, column_num)
                                    if type(self.board[row_num][column_num]) == list:
                                        self.check_box_unique(row_num, column_num, box_row, box_column)
            if all_filled:
                board_filled = True

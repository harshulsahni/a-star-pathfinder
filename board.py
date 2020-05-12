from cell import Cell


class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = [[]]
        self.board = self.make_board()

    def __repr__(self):
        return 'Board Object with {} rows and {} columns.'.format(self.width, self.height)

    def __str__(self):
        output = ''
        for row in self.board:
            row_str = ''
            for cell in row:
                row_str += '{}  '.format(cell)
            output += '{}\n'.format(row_str)

        return output

    def make_board(self):
        output = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(Cell.FREE)
            output.append(row)
        output[0][0] = Cell.OCCUPIED
        return output


class TicTacToeBoard:

    def __init__(self):
        self.matrix = [['', '', ''], ['', '', ''], ['', '', '']]
        self.player = 'x'
        self.check = 'None'

    def get_field(self):
        # print("")
        print(*self.matrix, sep="\n")

    def new_game(self):
        self.matrix = [['', '', ''], ['', '', ''], ['', '', '']]
        self.player = 'x'
        self.check = 'None'
        print("\nНовая игра начата")

    def check_field(self):
        end = '-'
        for i in self.matrix:
            if i[0] == 'x' and i[1] == 'x' and i[2] == 'x':
                return 'x'
            elif i[0] == 'o' and i[1] == 'o' and i[2] == 'o':
                return 'o'
            elif i[0] == '' or i[1] == '' or i[2] == '':
                end = ''
        i = 0
        while i < 3:
            if self.matrix[0][i] == 'x' and self.matrix[1][i] == 'x' and self.matrix[2][i] == 'x':
                return 'x'
            elif self.matrix[0][i] == 'o' and self.matrix[1][i] == 'o' and self.matrix[2][i] == 'o':
                return 'o'
            i += 1
        if self.matrix[0][0] == 'x' and self.matrix[1][1] == 'x' and self.matrix[2][2] == 'x':
            return 'x'
        elif self.matrix[0][2] == 'x' and self.matrix[1][1] == 'x' and self.matrix[2][0] == 'x':
            return 'x'
        elif self.matrix[0][0] == 'o' and self.matrix[1][1] == 'o' and self.matrix[2][2] == 'o':
            return 'o'
        elif self.matrix[0][2] == 'o' and self.matrix[1][1] == 'o' and self.matrix[2][0] == 'o':
            return 'o'
        elif end == '-':
            return 'D'
        else:
            return 'None'

    def make_move(self, row: int, col: int):
        if self.check == 'x' or self.check == 'o' or self.check == 'D':
            print("Игра уже завершена")
            return 0
        if self.matrix[row-1][col-1] != '':
            print(f"\nКлетка {row},{col} уже занята")
            return 0
        self.matrix[row-1][col-1] = self.player
        if self.player == 'x':
            self.player = 'o'
        else:
            self.player = 'x'
        self.check = self.check_field()
        if self.check == 'x':
            print("Победил игрок X!")
        elif self.check == 'o':
            print("Победил игрок O!")
        elif self.check == 'D':
            print("Ничья!")
        else:
            print("Продолжаем играть")

# board = TicTacToeBoard()
# board.get_field()
# board.make_move(1, 1)
# board.get_field()
# board.make_move(1, 1)
# board.make_move(1, 2)
# board.get_field()
# board.make_move(2, 1)
# board.make_move(2, 2)
# board.make_move(3, 1)
# board.make_move(2, 2)
# board.get_field()
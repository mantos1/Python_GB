class Table:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.table = {}
        self.new_table = {}

        for i in range(self.row):
            self.table[i] = [0 for ii in range(self.column)]

    def get_value(self, row, column):
        return self.table[row][column]

    def set_value(self, row, column, value):
        self.table[row][column] = value

    def n_rows(self):
        return self.row

    def n_cols(self):
        return self.column
        self.column = self.column - 1

    def delete_row(self, row):
        try:
            del self.table[row]
            i = 0
            for key, value in self.table.items():
                self.new_table[i] = value
                i += 1
            self.table = self.new_table
            self.row = key
            self.new_table = {}
        except:
            return

    def delete_col(self, column):
        try:
            for i in self.table:
               del self.table[i][column]
            self.column = self.column - 1
        except:
            return

    def add_row(self, row):
        if row >= self.row + 1: return
        for i in range(self.row + 1):

            if i < row and row <= self.row + 1:
                self.new_table[i] = [ii for ii in self.table[i]]
            elif i == row:
                self.new_table[i] = [0 for ii in range(self.column)]
            elif i > row:
                self.new_table[i] = [ii for ii in self.table[i-1]]
            else:
                self.new_table[i] = [0 for ii in range(self.column)]

        self.table = self.new_table
        self.row = self.row + 1
        self.new_table = {}

    def add_col(self, column):
        if column >= self.column + 1: return
        for i in self.table:
            self.table[i].insert(column, 0)
        self.column = self.column + 1

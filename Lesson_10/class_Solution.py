class Solution:
    def __init__(self, type):
        self.numbers = []
        self.result_int = 0
        self.result_float = 0.0
        self.type = type

    def add_number(self, number):
        number_str = str(number)
        if number_str.isdigit():
            self.numbers.append(int(number_str))

    def result(self):
        # 0 - MinStat
        # 1 - MaxStat
        # 2 - AverageStat
        try:
            if self.type == 0:
                return min(self.numbers)
            if self.type == 1:
                return max(self.numbers)
            if self.type == 2:
                return sum(self.numbers) / len(self.numbers)
        except:
            return None

class MinStat(Solution):
    def __init__(self):
        Solution.__init__(self, 0)

class MaxStat(Solution):
    def __init__(self):
        Solution.__init__(self, 1)

class AverageStat(Solution):
    def __init__(self):
        Solution.__init__(self, 2)

# # Пример 1.
# values = [1, 2, 4, 5]
# # values = [1, 0, 0]
# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# for v in values:
#     mins.add_number(v)
#     maxs.add_number(v)
#     average.add_number(v)
# print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

# # Пример 2.
# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# print(mins.result(), maxs.result(), average.result())

class PairedIterator:
    def __init__(self, data_list):
        self.data_list = data_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data_list) - 1:
            pair = (self.data_list[self.index], self.data_list[self.index + 1])
            self.index += 2
            return pair
        elif self.index == len(self.data_list) - 1:
            pair = (self.data_list[self.index], None)
            self.index += 2
            return pair
        else:
            raise StopIteration()

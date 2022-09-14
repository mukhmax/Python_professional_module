nested_list = [
    12,
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]


def list_flater(list_):
    for item in list_:
        if type(item) != list:
            yield item
        else:
            for item_ in list_flater(item):
                yield item_


class Iteration:
    def __init__(self, list_):
        self.list_ = list_
        # self.start = list_[0]
        # self.finish = list_[-1]

    def __iter__(self):
        self.cursor = -1
        self.counter = -1
        return self

    def __next__(self):
        if self.cursor >= len(self.list_)-1:
            raise StopIteration
        if isinstance(self.list_[self.cursor+1], list):
            if self.counter < len(self.list_[self.cursor+1]) - 2:
                self.counter += 1
                return self.list_[self.cursor+1][self.counter]
            else:
                self.cursor += 1
                self.counter = -1
                return self.list_[self.cursor][-1]
        else:
            self.cursor += 1
            return self.list_[self.cursor]


if __name__ == '__main__':
    # print(list(list_flater(nested_list)))

    flat_list = Iteration(nested_list)
    for el in flat_list:
        print(el)

    # print(count(nested_list))

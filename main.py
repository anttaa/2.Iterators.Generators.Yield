import types


# Задача № 1
class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list

    def __iter__(self):
        self.cursor_main = 0
        self.cursor_child = -1
        return self

    def __next__(self):
        self.cursor_child += 1

        if self.cursor_child == len(self.list[self.cursor_main]):
            self.cursor_main += 1
            self.cursor_child = 0

        if self.cursor_main == len(self.list):
            raise StopIteration

        return self.list[self.cursor_main][self.cursor_child]


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


# Задача № 2
def flat_generator(list_of_lists):
    for main_items in list_of_lists:
        for item in main_items:
            yield item


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item
    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


# Задача № 3
class FlatIteratorExt:

    def __init__(self, list_of_list):
        self.list = self.change(list_of_list)

    def change(self, value):
        res = []
        for item in value:
            if isinstance(item, list):
                res += self.change(item)
            else:
                res.append(item)
        return res

    def __iter__(self):
        self.cursor_main = -1
        return self

    def __next__(self):
        self.cursor_main += 1
        if self.cursor_main == len(self.list):
            raise StopIteration

        return self.list[self.cursor_main]


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIteratorExt(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item
    assert list(FlatIteratorExt(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


# Задача № 4
def flat_generator_ext(list_of_list):

    def change(value):
        res = []
        for item in value:
            if isinstance(item, list):
                res += change(item)
            else:
                res.append(item)
        return res

    for main_item in change(list_of_list):
        yield main_item


def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator_ext(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item
    assert list(flat_generator_ext(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    assert isinstance(flat_generator_ext(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()

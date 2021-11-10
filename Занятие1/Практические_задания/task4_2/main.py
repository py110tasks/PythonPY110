from itertools import count


def task():
    iterator_numbers = count(1, 1)
    numbers = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, iter))

    for num in numbers:  # TODO напечатать первые 10 чисел
        print(num)  # TODO с помощью next получать следующий элемент от итератора


if __name__ == "__main__":
    task()

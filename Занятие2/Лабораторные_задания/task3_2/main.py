def min_len_check(fn):
    # TODO записать обертку для исходной функции
    def wrapper(str_arg):
        if not isinstance(str_arg, str) or len(str_arg) < 10:
            raise ValueError("Строка слишком короткая")
        return fn(str_arg)
    return wrapper


# TODO задекорировать функцию
@min_len_check
def some_func(str_arg: str):
    return str_arg


if __name__ == "__main__":
    print(some_func("Hello, World!!!"))  # всё хорошо

    some_func("Short str")  # ValueError("Строка слишком короткая")

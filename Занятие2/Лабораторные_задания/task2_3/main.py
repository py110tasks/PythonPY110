def pow_gen(base: int):
    # TODO записать функцию-генератор
    #n = base
    s = 0
    while True:
        yield base ** s
        s += 1

if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))

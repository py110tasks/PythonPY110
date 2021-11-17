
def check(fn):
    def wrapper(*args):
        for a in args:
            if not isinstance(a, int):
                raise ValueError('Not int !')
        return fn(*args)
    return wrapper



@check
def func(*args):
    return sum(args)



if __name__ == "__main__":

    print(func(1,2,3,4,5,6))

    print(func(1,2,3,4,'a'))
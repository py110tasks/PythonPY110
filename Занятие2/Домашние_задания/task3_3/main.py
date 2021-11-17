def checkfn(fn):
    def wrapper(*a, **kw):
        for i in range(len(a)):
            try:
                (_ for _ in a[i])
            except:
                raise TypeError("Объект [%i]  не является итерируемым" % i)
        for k in kw:
            try:
                (_ for _ in kw[k])
            except:
                raise TypeError("Объект {%s} не является итерируемым" % k)
        return fn(*a, **kw)
    return wrapper

@checkfn
def fnc(*a, **kw):
    return True


if __name__ == "__main__":

    print(fnc([1,1], "qwerty", p1=(1,2,3)))

    print(fnc([1,1], p0=123, p1=(1,2,3)))
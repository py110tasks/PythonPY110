
def gp(step):
    gp = 1
    while True:
        yield gp
        gp *= step

if __name__ == "__main__":
    p = gp(2)
    for _ in range(10):
        print(next(p))
    pass

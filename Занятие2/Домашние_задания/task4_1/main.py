
def pw(pts):
    for i in range(len(pts)-1):
        yield pts[i], pts[i+1]

if __name__ == "__main__":
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]
    pws = pw(pts)
    res = sum(map(lambda a: ((a[0][0] - a[1][0]) ** 2 + (a[0][1] - a[1][1]) ** 2) ** 0.5, pws))
    print(res)
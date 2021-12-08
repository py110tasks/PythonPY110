from time import time, sleep


def average(cnt):
    count = cnt

    def make(fn):

        def decorator(*args, **kwargs):
            results = []
            for _ in range(count):
                sleep(1)  # для разных результатов.
                results.append(fn(*args, **kwargs))
            return sum(results)/count
        return decorator
    return make


@average(5)
def summary():
    a = int(time())
    print('--', a)
    return a


if __name__ == "__main__":
    print(summary())

# Output:
# -- 1638974956
# -- 1638974957
# -- 1638974958
# -- 1638974959
# -- 1638974960
# 1638974958.0

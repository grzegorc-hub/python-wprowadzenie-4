from time import time


def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print("elapsed", after - before)
        return rv
    return f

# add = timer(add)
@timer
def add(x, y=10):
    return x + y

@timer
def sub(x, y=10):
    return x - y


print(add(10))
print(add(20, 30))
print(add('a', 'b'))
print(sub(10))
print(sub(20, 30))

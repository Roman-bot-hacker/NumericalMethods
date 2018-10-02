import math

def f(z):
    return math.log(z)+z

def search_local_section(a, h):
    b = a + h
    fa = f(a)
    fb = f(b)
    if (abs(fb) > abs(fa))&(fa * fb > 0):
        h = - h
    b = a + h
    fb = f(b)
    while fa * fb > 0:
        a = b
        b = a + h
        fa = f(a)
        fb = f(b)
    return b

def iterate(a, b, eps):
    while True:
        x = (b + a)/2
        fa = f(a)
        fx = f(x)
        if fx * fa > 0:
            a = x
        else:
            b = x
        if abs(fx) < eps:
            return x


if __name__ == '__main__':
    a = 0.1
    h = 0.1
    eps = 0.01
    x = iterate(a, search_local_section(a, h), eps)
    print(str(x))
    res = f(x)
    print(str(res))
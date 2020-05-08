# extended GCD algorithm
def x_gcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

# multiplicative inverse mod n
def mod_inv(a, n):
    g, x, y = x_gcd(a, n)
    if g != 1:
        raise ValueError('mod_inv for {} does not exist'.format(a))
    return x % n

def get_s(a, p, x1, x2, y1, y2):
    if x1 == x2 and y1 == y2:
        s = ((x1**2 * 3 + a ) * mod_inv(2 * y1, p)) % p
    else:
        de = x2 - x1
        while de < 0:
            de += p
        s = ((y2 - y1) * mod_inv(de, p)) % p
    #print('s =', s)
    return s

def verify(x, y, a, b, p):
    return (y**2 % p) == ((x**3 + a * x + b) % p)

def elli_add(a, b, p, x1, y1, x2, y2):
    if (-y1) % p == y2 and x1 == x2:  # neutral element
        return 'neutral', 'element'
    else:
        s = get_s(a, p, x1, x2, y1, y2)
        x3 = (s ** 2 - x1 - x2) % p
        y3 = (s * (x1 - x3) - y1) % p
        return x3, y3

def q2():
    a = 2
    b = 2
    p = 17
    x1, y1 = 6, 3
    x2, y2 = 5, 1
    x3, y3 = elli_add(a, b, p, x1, y1, x2, y2)
    print(x3, y3)
    print(verify(x3, y3, a, b, p))

#q2()

def double_and_add(a, b, p, x, y, n):
    d = bin(n)[3:]  # remove '0b', start from the second bit
    xt, yt = x, y
    for i in d:
        xt, yt = elli_add(a, b, p, xt, yt, xt, yt)
        if i == '1':
            xt, yt = elli_add(a, b, p, xt, yt, x, y)
    return xt, yt

def q4():
    import numpy as np
    p = 1579602854473772853128287506817718026426265023617379175335587248616431
    lower = p + 1 - 2 * np.sqrt(float(p))
    higher = p + 1 + 2 * np.sqrt(float(p))
    print('bound', lower, higher)

    a = 654624412321892857559038596828572669649402987879847772735693306089759
    b = 563386056159714380473737077729260896240517015706612537779563193095411
    x = 953216670857201615849458843136747040308850692140282160349854110301248
    y = 187696769665068572312633292858802066603155820538026405642457554453538
    n = 230768357842901099381188113760304602568543491144769691849643435691536
    xt, yt = double_and_add(a, b, p, x, y, n)
    print(xt, yt)


q4()


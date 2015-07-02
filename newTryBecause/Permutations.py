__author__ = 'twi'
import itertools



def permute_wiktor(string, length):
    'Alternate version that filters from product()'
    pool = tuple(string)
    print(pool)
    n = len(pool)
    print(n)
    for indices in itertools.product(range(n), repeat=length):
        #print('--',indices)
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)


def product(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

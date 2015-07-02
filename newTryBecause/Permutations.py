__author__ = 'twi'
import itertools



def permute_wiktor(iterable, r):
    'Alternate version that filters from product()'
    pool = tuple(iterable)
    print(pool)
    n = len(pool)
    print(n)
    for indices in itertools.product(range(n), repeat=r):
        print('--',indices)
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)

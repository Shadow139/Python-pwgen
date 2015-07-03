__author__ = 'twi'

import itertools

permList = list(itertools.product("abcde", repeat = 12))  # This seems ok


for x in permList:
    print(x)
print(len(permList))

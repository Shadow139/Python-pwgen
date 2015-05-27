__author__ = 'twi'
import itertools

perm = []

# endless-loopcd
# string should be the charSet
# wiktor you idiot. len is length that permutations should be
# wiktor. string is which chracters
def buildIt(string,len):
    if (len < 1):
        return
    global perm
    count = 0
    while count < len:
        if perm == []:
            count += 1
            for x in string:
                perm.append(x)
        print(perm)
        for x in perm:
            print('hallo')
            for y in string:
                # filterin here??
                perm.append(x+y)
            if x in perm:
                perm.remove(x)
        count += 1
        print(count)
    print(perm)
# should be written into buffer and everything - right now it saves everything in an array and...yea.
# oh. and. filters.


def iter(string,length):
    permList =list(permus(string, length))
    #permList =list(permus(range(3)))

    for x in permList:
        print(x)
    print(len(permList))

def permus(string, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(string)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

def permus2(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in itertools.product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)
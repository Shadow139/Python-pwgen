__author__ = 'twi'

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

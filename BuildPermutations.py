__author__ = 'twi'

perm = []

# string should be the charSet
def buildIt(string,len):
    global perm
    count = 0
    while count < len:
        if perm == []:
            for x in string:
                perm.append(x)
        for x in perm:
            for y in string:
                # filterin here??
                perm.append(x+y)
            if x in perm:
                perm.remove(x)

# should be written into buffer and everything - right now it saves everything in an array and...yea.
# oh. and. filters.

import math

rawInput = open("input.txt").read()
_input = [int(x) for x in rawInput.split(",")]

length = 256
l = [x for x in range(length)]

def reverseFrom(_list,_startIndex,_length):
    fst = _startIndex
    lst = _startIndex + _length - 1 if _startIndex + _length - 1 < len(_list) else _startIndex + _length - len(_list) - 1
    for _ in range(math.floor(_length/2)):
        temp = _list[fst]
        _list[fst] = _list[lst]
        _list[lst] = temp

        fst += 1
        lst -= 1
        if fst >= len(_list):
            fst = 0
        if lst < 0:
            lst = len(_list) - 1


skipLength = 0
index = 0
for k in _input:
    reverseFrom(l,index,k)
    index = (index + k + skipLength) % len(l)
    skipLength += 1

print("Part 1: " + str(l[0]*l[1]))

l2 = [ord(c) for c in rawInput]
for x in [17,31,73,47,23]:
    l2.append(x)
# . . .
# Dont understand the how the question is phrased.
import re
from functools import reduce

_input = open("input.txt").read().split("\n")

entryList = []

class entry:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children

def getEntry(_list, _name):
    for e in _list:
        if e.name == _name: return e

for i in _input:
    name = re.split(" ", i)[0]
    weight = int(re.findall("\d+",i)[0])
    children = []
    if re.search("->",i):
        children = re.findall("\w+", re.split("->",i)[1])
    entryList.append(entry(name,weight,children))

# --- Part 1 ---
seenList = []
for e in entryList:
    seenList.append(e.name)

for e in entryList:
    for c in e.children:
        seenList.remove(c)

rootName = seenList[0]
print("Part 1: " + rootName)

# --- Part 2 ---
def getWeight(entry):
    childrenSum = 0
    weightList = []
    shouldRun = True
    for childName in entry.children:

        e = getEntry(entryList, childName)

        weight = getWeight(e)
        if weight == -1: 
            shouldRun = False
            break
        weightList.append(weight)
        childrenSum += weight

    if len(set(weightList)) > 1 and shouldRun:
        print(weightList)
        fst = 0
        snd = 0
        s = set(weightList)
        value = s.pop()
        for x in weightList:
            if x == value:
                fst += 1
            else:
                snd += 1
        if fst > snd: value = s.pop()
        
        t = set(weightList)
        diff = abs(t.pop() - t.pop())
        index = weightList.index(value)
        entryWrong = getEntry(entryList, entry.children[index])

        print(entryWrong.weight - diff)

        return -1

    return childrenSum + entry.weight 

for e in entryList:
    if e.name == rootName:
        root = e

getWeight(root)
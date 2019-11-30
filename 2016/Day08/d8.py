import operator

_input = open("input.txt").read().split("\n")

class reg:
    def __init__(self, name):
        self.name = name
        self.value = 0

def findOrCreateReg(_list, _name):
    found = False
    for r in _list:
        if r.name == _name:
            found = True
            register = r
    if not found:
        x = reg(_name)
        _list.append(x)
        register = x
    return register


registers = []
biggestValue = 0

for l in _input:
    arr = l.split(" ")
    
    conditionReg = arr[4]
    register = findOrCreateReg(registers, conditionReg)
    
    opStr = arr[5]
    opNum = int(arr[6])

    if opStr == ">":        
        op = operator.gt
    elif opStr == ">=":
        op = operator.ge
    elif opStr == "==":    
        op = operator.eq
    elif opStr == "<=":    
        op = operator.le
    elif opStr == "<":     
        op = operator.lt
    elif opStr == "!=":
        op = operator.ne
    
    if op(register.value, opNum):
        func = operator.add if arr[1] == "inc" else operator.sub
        register = findOrCreateReg(registers, arr[0])
        register.value = func(register.value, int(arr[2]))

    for r in registers:
        if r.value > biggestValue:
            biggestValue = r.value

val = registers[0].value
for r in registers:
    if r.value > val:
        val = r.value

print("Part 1: " + str(val))
print("Part 2: " + str(biggestValue))
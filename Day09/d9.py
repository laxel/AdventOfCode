_input = open("input.txt").read()

inGarbage = False
ignoreNext = False
numGarbage = 0
depth = 1
score = 0
for c in _input:
    if ignoreNext:
        ignoreNext = False
    else:
        if inGarbage:
            if c == ">":
                inGarbage = False
            elif c != "!":
                numGarbage += 1
        else:
            if c == "{":
                score += depth
                depth += 1
            elif c == "}":
                depth -= 1
            elif c == "<":
                inGarbage = True
        if c == "!":
                ignoreNext = True

print("Part 1: " + str(score))
print("Part 2: " + str(numGarbage))